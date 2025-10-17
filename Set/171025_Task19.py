names = {"Kumar", "Rakul", "Sukumar", "Ankush", "Rakesh", "Mukul", "Keerthi"}
ku_names = set()
for name in names:
    if "ku" in name.lower():
        ku_names.add(name)

print(ku_names)
