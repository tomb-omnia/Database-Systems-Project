DROP VIEW IF EXISTS StudentEnrollments;
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Courses;


CREATE TABLE IF NOT EXISTS Student (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT    NOT NULL,
    last_name  TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS Courses (
    course_id   INTEGER PRIMARY KEY,
    course_name TEXT    NOT NULL,
    credits     INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id    INTEGER NOT NULL,
    course_id     INTEGER NOT NULL,
    
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id)  REFERENCES Courses(course_id)
);


INSERT INTO Student (first_name, last_name) VALUES ('Alice',  'Johnson');
INSERT INTO Student (first_name, last_name) VALUES ('Bob',    'Smith');
INSERT INTO Student (first_name, last_name) VALUES ('Carlos', 'Rivera');
INSERT INTO Student (first_name, last_name) VALUES ('Diana',  'Lee');
INSERT INTO Student (first_name, last_name) VALUES ('Ethan',  'Brown');


INSERT INTO Courses (course_name, credits) VALUES ('database systems', 3);
INSERT INTO Courses (course_name, credits) VALUES ('devOps', 3);
INSERT INTO Courses (course_name, credits) VALUES ('calculus I', 4);
INSERT INTO Courses (course_name, credits) VALUES ('computer systems', 3);
INSERT INTO Courses (course_name, credits) VALUES ('data structures and algorithms', 3);


INSERT INTO Enrollments (student_id, course_id) VALUES (1, 1);
INSERT INTO Enrollments (student_id, course_id) VALUES (1, 2);
INSERT INTO Enrollments (student_id, course_id) VALUES (2, 1);
INSERT INTO Enrollments (student_id, course_id) VALUES (2, 3);
INSERT INTO Enrollments (student_id, course_id) VALUES (3, 2);
INSERT INTO Enrollments (student_id, course_id) VALUES (3, 4);
INSERT INTO Enrollments (student_id, course_id) VALUES (4, 3);
INSERT INTO Enrollments (student_id, course_id) VALUES (4, 5);
INSERT INTO Enrollments (student_id, course_id) VALUES (5, 1);
INSERT INTO Enrollments (student_id, course_id) VALUES (5, 4);


CREATE VIEW IF NOT EXISTS StudentEnrollments AS
SELECT
    Student.student_id,
    Student.first_name,
    Student.last_name,
    Courses.course_id,
    Courses.course_name,
    Courses.credits
FROM Enrollments
JOIN Student ON Enrollments.student_id = Student.student_id
JOIN Courses ON Enrollments.course_id  = Courses.course_id;