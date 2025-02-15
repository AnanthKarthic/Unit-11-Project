import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("youtubeChannel.csv")



data["Subscribers (Million)"] = pd.to_numeric(data["Subscribers (Million)"])
data["Uploads"] = pd.to_numeric(data["Uploads"])
data["Views"] = pd.to_numeric(data["Views"])
data["Ranking"] = pd.to_numeric(data["Ranking"])

#Sets up the 1x3 axis for all the graphs
ig, axes = plt.subplots(3, 1, figsize=(10, 15))  # 3 rows, 1 column

# Graph 1: Subscribers vs Views
axes[0].scatter(data["Subscribers (Million)"], data["Views"], alpha=0.5)
axes[0].set_title("Subscribers vs Views")
axes[0].set_xlabel("Subscribers (Million)")
axes[0].set_ylabel("Views")

axes[0].set_xlim(40, 150)
axes[0].set_ylim(0, 1.5e11)

# Graph 2: Subscribers vs Uploads
axes[1].scatter(data["Subscribers (Million)"], data["Uploads"], alpha=0.5)
axes[1].set_title("Subscribers vs Uploads")
axes[1].set_xlabel("Subscribers (Million)")
axes[1].set_ylabel("Uploads")

axes[1].set_xlim(40, 100)  # Zoom into channels with up to 100 million subscribers
axes[1].set_ylim(0, 30000) # Zoom into channels with up to 30k uploads

# Graph 3: Views vs Uploads
axes[2].scatter(data["Views"], data["Uploads"], alpha=0.5)
axes[2].set_title("Views vs Uploads")
axes[2].set_xlabel("Views")
axes[2].set_ylabel("Uploads")

axes[2].set_xlim(0, 4.6e10)  # Focus on channels with up to 46 billion views
axes[2].set_ylim(0, 30000)  # Focus on channels with fewer than 30000 uploads


#Calculates avg for these values
avg_subscribers = data["Subscribers (Million)"].mean()
avg_uploads = data["Uploads"].mean()
avg_views = data["Views"].mean()

#Display/output code
print("")
print("\t\t\t\tAn Analysis of Top 100 YouTube Channels")
print("\t\t\t\t -------------------------------------")
print("\nAverage Statistics:")
print(f"Average Subscribers: {avg_subscribers:.2f} million")
print(f"Average Uploads: {avg_uploads:.0f}")
print(f"Average Views: {avg_views:.0f}")
print("")
print(data.head())
print("")
print("\t\t\t\t...")
print("")
print(data.tail())
plt.savefig("youtube_analysis.png")
plt.show()