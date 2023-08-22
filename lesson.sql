'''Show the full name of the teacher who is teaching the Programming subject (with subquery).'''
SELECT f_name, l_name
FROM TEACHERS
WHERE teacher_id = (SELECT teacher_id FROM SUBJECTS WHERE subject_id = 2);

'''Show the subject names where student 4 is enrolled.'''
SELECT S.subject_name
FROM SUBJECTS S, ENROLLMENTS E
WHERE S.subject_id = E.subject_id
AND E.student_id = 4

'''Show students full name and email that are enrolled in subject 2.'''
SELECT f_name, l_name, email
FROM STUDENTS S, ENROLLMENTS E
WHERE S.student_id = E.student_id
AND E.subject_id = 2;

`Show a list with students full name, enrolment date and subject name.`
SELECT S.f_name as "first name", S.l_name as "last name", E.enrollment_date as "Start date", C.subject_name as "Course"
FROM STUDENTS S, ENROLLMENTS E, SUBJECTS C
WHERE S.student_id = E.student_id
AND C.subject_id = E.subject_id;


`Show a list with students full name, enrolment date, subject name and the teacher's name teaching each subject.`
SELECT S.f_name as "Student first name", S.l_name as "Student last name", E.enrollment_date, C.subject_name, T.f_name as "Teacher first name", T.l_name as "Teacher last name"
FROM STUDENTS S, ENROLLMENTS E, SUBJECTS C, TEACHERS T
WHERE S.student_id = E.student_id
AND E.subject_id = C.subject_id
AND T.teacher_id = C.teacher_id;

`Show a list with students full name, enrolment date, subject name and the teacher's name teaching each subject.`
SELECT CONCAT(S.f_name, ' ', S.l_name) AS "student", E.enrollment_date, C.subject_name, CONCAT(T.f_name, ' ', T.l_name) AS "teacher"
FROM STUDENTS S, ENROLLMENTS E, SUBJECTS C, TEACHERS T
WHERE S.student_id = E.student_id
AND E.subject_id = C.subject_id
AND T.teacher_id = C.teacher_id;