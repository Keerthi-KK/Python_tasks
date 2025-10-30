class student:
    def __init__(self,name,roll_num,marks):
        self.name=name
        self.roll_num=roll_num
        self.marks=marks
    def student_details(self):
        print("Student name",self.name)
        print("Student roll number",self.roll_num)
        print("Student marks",self.marks)
    def student_avg(self):
        total_mark=sum(self.marks.values())
        total=len(self.marks)
        avg=total_mark/total
        return avg
    def student_grade(self):
        total_mark=sum(self.marks.values())
        total=len(self.marks)
        avg=total_mark/total

        if avg>=90:
            return "A"
        elif avg<90 and avg>=80:
            return "B"
        else: return "C"
kiran =student("kiran",18902,{"Tamil":99,"English":89,"Maths":80})
Nisha =student("Nisha",18912,{"Tamil":97,"English":78,"Maths":76})

for i in [kiran,Nisha]:
               i.student_details()
               print(i.student_avg())
               print(i.student_grade())
               
