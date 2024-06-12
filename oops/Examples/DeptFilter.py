class Employee:
    
    def __init__(self, data) -> None:
        self.objData = data

    def filter(self, keyword):
        result = []
        for emp in self.objData:
            if emp["dept"] == keyword:
                result.append(emp)
        return result

data = [ 
            {"name" : "Ram", "age" : 25, "salary": 12000, "dept":"it"},
            {"name" : "Shyam", "age" : 15, "salary": 12000, "dept":"it"},
            {"name" : "Ravan", "age" : 55, "salary": 12000, "dept":"doctor"},
            {"name" : "Laxman", "age" : 45, "salary": 12000, "dept":"mechanic"},
            {"name" : "Peter", "age" : 75, "salary": 12000, "dept":"mechanic"},
        ]

report = Employee(data)
print(report.filter("it"))