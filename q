[33mcommit 73e48713b605da38ebf8e00b617a6cbe4621bbe8[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmain[m[33m, [m[1;33mtag: [m[1;33mv1.0.0[m[33m)[m
Author: vince <vince.dev@icloud.com>
Date:   Sat Jun 22 13:44:56 2024 -0700

    Add feature for MySQL database initialization
    
    - Implemented `InitDB` script to automate MySQL database setup.
    - Includes user input for database configuration, SQL script generation,
      execution via subprocess, and secure credential management.
    - Logs script execution details to `init_db.log` for monitoring.
    - Writes database credentials to `.env` file with secure permissions.
    - Validates database connectivity post-setup to ensure functionality.

[33mcommit c50b7a8ff0cb3b2494e519c7be6bd74a5dfddac5[m
Merge: a338a20 4b9ee90
Author: vince <vince.dev@icloud.com>
Date:   Sat Jun 22 09:03:34 2024 -0700

    Merge branch 'wip'

[33mcommit a338a20b6ba20e29b8bfd3bf4fbc939f78812ee3[m[33m ([m[1;31morigin/main[m[33m)[m
Author: devinci-it <vince.it@icloud.com>
Date:   Mon Apr 29 02:10:35 2024 -0700

    Merged changes from 'wip' branch for 'stubs' directory

[33mcommit 4b9ee90a3db800ba9041c571ead0ab8d57fcdc61[m[33m ([m[1;32mwip[m[33m)[m
Author: devinci-it <vince.it@icloud.com>
Date:   Mon Apr 29 02:07:18 2024 -0700

    added:documentation stubs

[33mcommit 8b4e0077a64dc3065e5c3d10fb2fbf52a38839eb[m
Author: devinci-it <vince.it@icloud.com>
Date:   Mon Apr 29 01:06:36 2024 -0700

    "Implemented automated class generation with customizable attributes, methods, getters, and setters. Updated documentation to reflect the changes."

[33mcommit 235f7938a22a3fa9c160da3945c15c182f1e5725[m
Author: devinci-it <vince.it@icloud.com>
Date:   Mon Apr 29 00:08:01 2024 -0700

            modified:   .gitignore
            modified:   LICENSE
            modified:   README.md#
            new file:   config.ini
            deleted:    devinci
            modified:   requirements.txt
            new file:   run.py
            modified:   setup.py
            deleted:    src/App/cli.py
            new file:   src/__init__.py
            new file:   src/app/__init__.py
            new file:   src/app/app.py
            renamed:    src/App/__init__.py -> src/app/term.py
            new file:   src/cli/__init__.py
            new file:   src/cli/cli.py
            new file:   src/config/__init__.py
            new file:   src/config/config.py
            new file:   src/log/__init__.py
            new file:   src/log/log.py
            new file:   storage/logs/.gitignore
            new file:   utils/__init__.py
            new file:   utils/autoload.py
            renamed:    src/App/app.py -> utils/env_setup.py

[33mcommit 3ca83a2e8210cf69484081f16fe5b01e769d5cc9[m
Author: devinci-it <vince.it@icloud.com>
Date:   Wed Apr 24 22:18:08 2024 -0700

    v0.0.1:draft `devinci` tool

[33mcommit c485ba2d00a18f95aa24d8ab80481f1d1ff9b95a[m
Author: devinci-it <vince.it@icloud.com>
Date:   Wed Apr 24 22:16:41 2024 -0700

    added gitignore
