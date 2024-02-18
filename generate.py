import os
import dotenv

dotenv.load_dotenv()

puml_java = os.getenv("JAVA_PUML_PATH")
puml_dir = "./src/"
docs_dir = "./docs/"
cmd = f"java -jar {puml_java} -tsvg {puml_dir}"

puml_files = os.listdir(puml_dir)

for puml_file in puml_files:
    if not puml_file.endswith(".puml"):
        continue

    os.system(cmd + puml_file)  # Генерируем SVG

    os.rename(puml_dir + puml_file[:-5] + ".svg", docs_dir + puml_file[:-5] + ".svg")
