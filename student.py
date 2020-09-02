from dataclasses import dataclass
@dataclass
class student:
    name: str
    college_id: int
    gpa:float

    def __str__(self):
        return f'Name {self.name}. GPA:{self.gpa}'

def main():
    filmon=student('filmon','12345','3.7')
    print(filmon)
    dave=student('dave','09876','3.0')
    print(dave)
    gigi=student('gigi','67890','3.4')
    print(gigi)

main()    
