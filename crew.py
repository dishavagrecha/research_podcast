from datetime import datetime
import os
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, before_kickoff, crew, task
from tools import file_reader_tool, voice_tool  


@CrewBase
class ResearchCrew:
    """Crew that takes in a PDF research paper and outputs a narrated podcast."""

    # === Agents ===
    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config["researcher"], verbose=True)

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(config=self.agents_config["reporting_analyst"], verbose=True)

    @agent
    def script_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["script_writer"],
            tools=[file_reader_tool],
            verbose=True
        )

    @agent
    def narrator(self) -> Agent:
        return Agent(
            config=self.agents_config["narrator"],
            tools=[voice_tool],
            verbose=True
        )

    # === Tasks ===
    @before_kickoff
    def _ensure_outputs_dir(self, inputs):
        os.makedirs(os.path.join(os.getcwd(), "outputs"), exist_ok=True)
        return inputs

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"]
        )

    @task
    def reporting_task(self) -> Task:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        return Task(
            config=self.tasks_config["reporting_task"]
            # output_file=f"outputs/report-{timestamp}.md"
        )

    @task
    def script_task(self) -> Task:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        return Task(
            config=self.tasks_config["script_task"],
            output_file=f"outputs/script-{timestamp}.md"
        )

    @task
    def narration_task(self) -> Task:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        return Task( 
            config=self.tasks_config["narration_task"],
            output_file=f"outputs/narration-{timestamp}.mp3" 
            )

    # === Crew Runner ===
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )


