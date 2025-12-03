"""
Simple Machine Learning Introduction Script
Dec 3, 2025
Made With <3 By Muhammad Walid
"""

def main():

    print("Welcome to Machine Learning with Python!")
    print("This is my first ML project in the Amit Repo.")

    DEPI_topics = ["Math", "Python", "Preprocessing & Visualization", "Machine Learning", "Deep Learning", "NLP", "Computer Vision", "AZure", "MI-Flow"]

    print("\nese are the topics we're going to learn in the next 6 months :)", "#" * 65, sep="\n")
    for counter, topic in enumerate(DEPI_topics, 1):

        print(f"{counter}- {topic}")

    print("Enjoy The Journey <3")

if __name__ == "__main__":

    main()