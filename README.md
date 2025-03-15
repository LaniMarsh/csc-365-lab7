# csc-365-lab7

Group Members - 
Lani Marsh
Lambert Zhang


To run the program simply run main.py


##Git Log
commit 0b79e3ef011d27848ae2896378ed3cc791d6c513 (HEAD -> main, origin/main, origin/HEAD)
Author: LaniMarsh <lmarsh12@calpoly.edu>
Date:   Fri Mar 14 22:10:30 2025 -0700

    Fix minor bug issue

 database.py     | 2 +-
 main.py         | 4 ++--
 reservations.py | 8 +++++++-
 3 files changed, 10 insertions(+), 4 deletions(-)

commit ec4e780b539b93dddd956fe2f2432440cfbaf823
Merge: 7d5b5df 7395280
Author: LaniMarsh <lmarsh12@calpoly.edu>
Date:   Fri Mar 14 21:59:23 2025 -0700

    Merge remote-tracking branch 'origin/fixed-res'

commit 7d5b5dfcd37404bd326006ca86aa7c5222843c0f
Author: LaniMarsh <lmarsh12@calpoly.edu>
Date:   Fri Mar 14 13:38:39 2025 -0700

    fix some minor bugs and add test data for cli testing

 database.py     | 49 +++++++++++++++++++++++++++++++++++++++++++++----
 main.py         |  2 ++
 reservations.py | 18 ++++++++++++------
 rooms.py        | 16 ++++++++++------
 4 files changed, 69 insertions(+), 16 deletions(-)

commit 1e3849b0ae19016dfcb744c5709eed7d8471e182
Author: LaniMarsh <122917983+LaniMarsh@users.noreply.github.com>
Date:   Fri Mar 14 12:51:46 2025 -0700

    Update README.md

 README.md | 6 +++++-
 1 file changed, 5 insertions(+), 1 deletion(-)

commit 7395280e487368b7439c703cf26197476045ac08 (origin/fixed-res)
Author: lambertzz <zjzhangg@gmail.com>
Date:   Fri Mar 14 11:53:22 2025 -0700

    fixed reservation function

 reservations.py | 108 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---------------------------------------
 1 file changed, 69 insertions(+), 39 deletions(-)

commit 8d0e1c2302155bb48b06c01f948f43532b69d19c
Author: LaniMarsh <lmarsh12@calpoly.edu>
Date:   Fri Mar 14 02:16:45 2025 -0700

    Add reservations, rooms, and revenue files with functions. Making a reservation does not work, the unit test doesn't pass

 .gitignore      |  1 +
 main.py         | 30 ++++++++++++++++++++++++++++++
 reservations.py | 94 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 revenue.py      | 25 +++++++++++++++++++++++++
 rooms.py        | 33 +++++++++++++++++++++++++++++++++
 tests.py        | 92 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 6 files changed, 275 insertions(+)

commit a9bd8d608dd8b90ee3ecf4309bf6131e9b01b37a
Author: LaniMarsh <lmarsh12@calpoly.edu>
Date:   Thu Mar 13 23:05:11 2025 -0700

    Set up tables

 .idea/.gitignore                                                                                               |    8 +
 .idea/csc-365-lab7.iml                                                                                         |    8 +
 .idea/inspectionProfiles/profiles_settings.xml                                                                 |    6 +
 .idea/misc.xml                                                                                                 |    7 +
 .idea/modules.xml                                                                                              |    8 +
 .idea/vcs.xml                                                                                                  |    6 +
 database.py                                                                                                    |   71 +
 main.py                                                                                                        |    0
... added venv setup files
 1041 files changed, 177998 insertions(+)

commit 28f945651a382f41b1eca475dec0ffa3fe5b5cfa
Author: LaniMarsh <122917983+LaniMarsh@users.noreply.github.com>
Date:   Thu Mar 13 22:02:08 2025 -0700

    Initial commit

 README.md | 1 +
 1 file changed, 1 insertion(+)
