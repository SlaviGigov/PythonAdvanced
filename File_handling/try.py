import os


def extract_files(dir):
    return [el for el in dir_content if "." in el]


def get_report_for_extensions(files):
    report = {}
    for file in files:
        name, extension = file.split(".")
        if extension not in report:
            report[extension] = []
        report[extension].append(name)
    return report


dir_content = os.listdir()

files = extract_files(dir_content)
report_info = get_report_for_extensions(files)

result_str = ""
for extension, file_names in sorted(report_info.items(), key=lambda x: x[0]):
    result_str += f".{extension}\n"
    for name in file_names:
        result_str += f"- - - {name}.{extension}\n"

with open("C:\\User\\User\\Desktop\\my_report.txt", "w") as file:
    file.write(result_str)
