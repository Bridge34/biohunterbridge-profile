# about_me.py - professional beginner portfolio script
def profile():
    name = "Bridge34"
    email = "biohunterbridge@gmail.com"
    location = "Rwanda"
    skills = ["Linux", "Git", "Kali Linux", "Bash", "Python", "NixOS (learning)"]
    projects = ["my-first-git", "Security-lab (coming soon)", "Portfolio demo"]

    print("=== Bridge34 Portfolio Script ===")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Location: {location}")
    print("Skills: " + ", ".join(skills))
    print("Projects: " + ", ".join(projects))
    print("Keep following my progress!")

if __name__ == "__main__":
    profile()
