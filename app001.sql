BEGIN;
--
-- Create model Country
--
CREATE TABLE "main_country" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "country_name" varchar(30) NOT NULL);
--
-- Create model MathSubjectClass
--
CREATE TABLE "main_mathsubjectclass" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "math_subject_class_name" varchar(80) NOT NULL);
--
-- Create model University
--
CREATE TABLE "main_university" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "university_name" varchar(80) NOT NULL);
--
-- Create model Mathematician
--
CREATE TABLE "main_mathematician" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(30) NOT NULL, "middle_mane" varchar(30) NULL, "last_name" varchar(30) NOT NULL, "year_of_degree" integer NOT NULL, "country_id_id" integer NOT NULL REFERENCES "main_country" ("id") DEFERRABLE INITIALLY DEFERRED, "math_subject_class_id_id" integer NOT NULL REFERENCES "main_mathsubjectclass" ("id") DEFERRABLE INITIALLY DEFERRED, "university_id_id" integer NOT NULL REFERENCES "main_university" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model StudentAdvisor
--
CREATE TABLE "main_studentadvisor" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "advisor_id" integer NOT NULL REFERENCES "main_mathematician" ("id") DEFERRABLE INITIALLY DEFERRED, "student_id" integer NOT NULL REFERENCES "main_mathematician" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "main_mathematician_country_id_id_9ff8e47f" ON "main_mathematician" ("country_id_id");
CREATE INDEX "main_mathematician_math_subject_class_id_id_f1fbbc67" ON "main_mathematician" ("math_subject_class_id_id");
CREATE INDEX "main_mathematician_university_id_id_565f3172" ON "main_mathematician" ("university_id_id");
CREATE UNIQUE INDEX "main_studentadvisor_student_id_advisor_id_0fc4f6f1_uniq" ON "main_studentadvisor" ("student_id", "advisor_id");
CREATE INDEX "main_studentadvisor_advisor_id_aa1dbe81" ON "main_studentadvisor" ("advisor_id");
CREATE INDEX "main_studentadvisor_student_id_b8c8fdf2" ON "main_studentadvisor" ("student_id");
COMMIT;
