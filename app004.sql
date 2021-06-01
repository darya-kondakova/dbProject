BEGIN;
--
-- Create model Article
--
CREATE TABLE "main_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "article_name" varchar(200) NOT NULL);
--
-- Create model Dissertation
--
CREATE TABLE "main_dissertation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "dissertation_name" varchar(200) NOT NULL);
--
-- Create model Magazine
--
CREATE TABLE "main_magazine" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "magazine_name" varchar(200) NOT NULL);
--
-- Alter field year_of_degree on mathematician
--
CREATE TABLE "new__main_mathematician" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(30) NOT NULL, "middle_mane" varchar(30) NULL, "last_name" varchar(30) NOT NULL, "country_id_id" integer NOT NULL REFERENCES "main_country" ("id") DEFERRABLE INITIALLY DEFERRED, "math_subject_class_id_id" integer NOT NULL REFERENCES "main_mathsubjectclass" ("id") DEFERRABLE INITIALLY DEFERRED, "university_id_id" integer NOT NULL REFERENCES "main_university" ("id") DEFERRABLE INITIALLY DEFERRED, "year_of_degree" integer NULL);
INSERT INTO "new__main_mathematician" ("id", "first_name", "middle_mane", "last_name", "country_id_id", "math_subject_class_id_id", "university_id_id", "year_of_degree") SELECT "id", "first_name", "middle_mane", "last_name", "country_id_id", "math_subject_class_id_id", "university_id_id", "year_of_degree" FROM "main_mathematician";
DROP TABLE "main_mathematician";
ALTER TABLE "new__main_mathematician" RENAME TO "main_mathematician";
CREATE INDEX "main_mathematician_country_id_id_9ff8e47f" ON "main_mathematician" ("country_id_id");
CREATE INDEX "main_mathematician_math_subject_class_id_id_f1fbbc67" ON "main_mathematician" ("math_subject_class_id_id");
CREATE INDEX "main_mathematician_university_id_id_565f3172" ON "main_mathematician" ("university_id_id");
--
-- Add field dissertation_id to mathematician
--
CREATE TABLE "new__main_mathematician" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(30) NOT NULL, "middle_mane" varchar(30) NULL, "last_name" varchar(30) NOT NULL, "year_of_degree" integer NULL, "country_id_id" integer NOT NULL REFERENCES "main_country" ("id") DEFERRABLE INITIALLY DEFERRED, "math_subject_class_id_id" integer NOT NULL REFERENCES "main_mathsubjectclass" ("id") DEFERRABLE INITIALLY DEFERRED, "university_id_id" integer NOT NULL REFERENCES "main_university" ("id") DEFERRABLE INITIALLY DEFERRED, "dissertation_id_id" integer NULL REFERENCES "main_dissertation" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__main_mathematician" ("id", "first_name", "middle_mane", "last_name", "year_of_degree", "country_id_id", "math_subject_class_id_id", "university_id_id", "dissertation_id_id") SELECT "id", "first_name", "middle_mane", "last_name", "year_of_degree", "country_id_id", "math_subject_class_id_id", "university_id_id", NULL FROM "main_mathematician";
DROP TABLE "main_mathematician";
ALTER TABLE "new__main_mathematician" RENAME TO "main_mathematician";
CREATE INDEX "main_mathematician_country_id_id_9ff8e47f" ON "main_mathematician" ("country_id_id");
CREATE INDEX "main_mathematician_math_subject_class_id_id_f1fbbc67" ON "main_mathematician" ("math_subject_class_id_id");
CREATE INDEX "main_mathematician_university_id_id_565f3172" ON "main_mathematician" ("university_id_id");
CREATE INDEX "main_mathematician_dissertation_id_id_5e84a0a3" ON "main_mathematician" ("dissertation_id_id");
--
-- Create model MagazineArticle
--
CREATE TABLE "main_magazinearticle" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "article_id" integer NOT NULL REFERENCES "main_article" ("id") DEFERRABLE INITIALLY DEFERRED, "magazine_id" integer NOT NULL REFERENCES "main_magazine" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model ArticleMathematician
--
CREATE TABLE "main_articlemathematician" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "article_id" integer NOT NULL REFERENCES "main_article" ("id") DEFERRABLE INITIALLY DEFERRED, "mathematician_id" integer NOT NULL REFERENCES "main_mathematician" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "main_magazinearticle_article_id_magazine_id_bca9c03d_uniq" ON "main_magazinearticle" ("article_id", "magazine_id");
CREATE INDEX "main_magazinearticle_article_id_c013f8cb" ON "main_magazinearticle" ("article_id");
CREATE INDEX "main_magazinearticle_magazine_id_d664e6be" ON "main_magazinearticle" ("magazine_id");
CREATE UNIQUE INDEX "main_articlemathematician_article_id_mathematician_id_e2d7df3b_uniq" ON "main_articlemathematician" ("article_id", "mathematician_id");
CREATE INDEX "main_articlemathematician_article_id_75fc2fbd" ON "main_articlemathematician" ("article_id");
CREATE INDEX "main_articlemathematician_mathematician_id_bcbf1359" ON "main_articlemathematician" ("mathematician_id");
COMMIT;
