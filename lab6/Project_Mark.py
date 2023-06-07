class ProjectEstimation:
    def __init__(self, a, m, b):
        self.a = a
        self.m = m
        self.b = b

    def Task_Main_calculate(self):
        E = (self.a + 4 * self.m + self.b) / 6
        SD = (self.b - self.a) / 6
        return E, SD
   
    def E_SD_AllProject(self, tasks):
        total_E = 0
        total_SD = 0
        for task in tasks:
            E, SD = task.Task_Main_calculate()
            total_E += E #додаєм E для оцінок кожного завдання
            total_SD += SD ** 2  # квадрати відхилень

        E_project = total_E
        SE_project = (total_SD ** 0.5) / len(tasks) #розраховує помилку проекту на основі усіх оцінок
        return E_project, SE_project

    def interval(self, E_project, SE_project):
        lower = E_project - 2 * SE_project
        upper = E_project + 2 * SE_project
        return lower, upper


# Отримання даних від користувача
tasks = []
num_tasks = int(input("Введіть кількість завдань: "))

for i in range(num_tasks):
    print(f"Завдання {i+1}:")
    a = float(input("Введіть оцінку a: "))
    m = float(input("Введіть оцінку m: "))
    b = float(input("Введіть оцінку b: "))
    tasks.append(ProjectEstimation(a, m, b))

# Розрахунок оцінки проекту
project = ProjectEstimation(0, 0, 0)
E_project, SE_project = project.E_SD_AllProject(tasks)
lower, upper = project.interval(E_project, SE_project)

# Виведення результатів
print("Результати оцінки проекту:")
print(f"E(project): {E_project}")
print(f"SE(project): {SE_project}")
print(f"Project's 95% confidence interval: {lower} ... {upper} points")