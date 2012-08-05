CREATE TABLE img_list (id INTEGER PRIMARY KEY NOT NULL,
                       path TEXT, mtime TEXT NOT NULL UNIQUE, 
                       md5 TEXT NOT NULL UNIQUE) ;
