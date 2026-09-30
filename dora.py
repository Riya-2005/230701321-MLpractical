import matplotlib.pyplot as plt

weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
deployments = [8, 12, 5, 20, 10]
lead_days = [2.4, 1.8, 3.2, 1.2, 2.0]
failures = [1, 2, 1, 2, 1]
restore_hours = [4, 3, 8, 2, 5]
failure_rate = [failed / total * 100 for failed, total in zip(failures, deployments)]

metrics = [
	("Deployment frequency", deployments, "deployments/week"),
	("Lead time for changes", lead_days, "days"),
	("Change failure rate", failure_rate, "%"),
	("Time to restore service", restore_hours, "hours"),
]
fig, axes = plt.subplots(2, 2, figsize=(10, 6))
for ax, (title, values, unit) in zip(axes.flat, metrics):
	ax.bar(weeks, values, color="#247a73")
	ax.set(title=title, ylabel=unit)
	ax.grid(axis="y", alpha=0.25)
fig.tight_layout()
plt.show()