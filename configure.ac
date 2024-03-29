AC_INIT([fastresolve],[2.11])
AM_INIT_AUTOMAKE
AC_ARG_PROGRAM
AC_PATH_PROGS(PERL, [perl5 perl], [/usr/bin/perl])
AC_PROG_CC
AC_PROG_CXX
AC_CHECK_FUNCS(fgetln)

# The following macro is
#    Copyright (C) 1997-1999 Ian Jackson <ian@davenant.greenend.org.uk>
# distributed under the GNU GPL (v2+).
AC_DEFUN([ADNS_C_GETFUNC],[
 AC_CHECK_FUNC([$1],,[
  AC_CHECK_LIB([$2],[$1],[$3],[
    AC_MSG_ERROR([cannot find library function $1])
  ])
 ])
])

ADNS_C_GETFUNC(socket,socket)
ADNS_C_GETFUNC(inet_ntoa,nsl)
ADNS_C_GETFUNC(inet_aton,resolv,[LIBS="-lresolv $LIBS"])
AC_CHECK_LIB(z, gzprintf, , AC_MSG_ERROR([zlib including gzprintf is required]))
AC_CHECK_LIB(adns, adns_submit, , AC_MSG_ERROR([adns library is required]))

AC_DEFUN([DJM_LIB_DB_CXX],
[dnl Check for a C++ interface, either version.

dnl Berkeley DB 2.x.
AC_CACHE_CHECK([for Db::open in -ldb], djm_cv_lib_db_Dbopen,
[AC_LANG_SAVE
AC_LANG([C++])
djm_save_LIBS="$LIBS"
LIBS="$LIBS -ldb"
AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <db_cxx.h>]], [[Db::open(NULL, DB_BTREE, DB_CREATE, 0, NULL, NULL, NULL);]])],[djm_cv_lib_db_Dbopen=yes],[djm_cv_lib_db_Dbopen=no])
LIBS="$djm_save_LIBS"
AC_LANG_RESTORE])

if test $djm_cv_lib_db_Dbopen = yes; then
	LIBS="$LIBS -ldb"
else

dnl The Db::open prototype changed in db-4.1, gaining the transaction ID parameter:
dnl db-3.3.11: int Db::open(const char *file, const char *database, DBTYPE type, u_int32_t flags, int mode)
dnl db-4.0.14: int Db::open(const char *file, const char *database, DBTYPE type, u_int32_t flags, int mode)
dnl db-4.1.25: int Db::open(DbTxn *txnid, const char *file, const char *database, DBTYPE type, u_int32_t flags, int mode)
dnl db-4.4.20: int Db::open(DbTxn *txnid, const char *file, const char *database, DBTYPE type, u_int32_t flags, int mode)
dnl db-4.8.30: int Db::open(DbTxn *txnid, const char *file, const char *database, DBTYPE type, u_int32_t flags, int mode)
dnl db-5.3.28: int Db::open(DbTxn *txnid, const char *file, const char *database, DBTYPE type, u_int32_t flags, int mode)
dnl db-6.1.19: int Db::open(DbTxn *txnid, const char *file, const char *database, DBTYPE type, u_int32_t flags, int mode)

dnl Berkeley DB 3.x-4.0 installed as libdb and libdb_cxx.
AC_CACHE_CHECK([for Db::open 3.x-4.0 in -ldb_cxx], djm_cv_lib_db_cxx_Dbopen_34,
[AC_LANG_SAVE
AC_LANG([C++])
djm_save_LIBS="$LIBS"
LIBS="$LIBS -ldb -ldb_cxx"
AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <db_cxx.h>]], [[Db *d = new Db(NULL, 0);
d->open(NULL, NULL, DB_BTREE, DB_CREATE, 0);]])],[djm_cv_lib_db_cxx_Dbopen_34=yes],[djm_cv_lib_db_cxx_Dbopen_34=no])
LIBS="$djm_save_LIBS"
AC_LANG_RESTORE])

if test $djm_cv_lib_db_cxx_Dbopen_34 = yes; then
	LIBS="$LIBS -ldb -ldb_cxx"
else

dnl Berkeley DB 3.x installed as libdb3 (as on FreeBSD).
AC_CACHE_CHECK([for Db::open in -ldb3_cxx], djm_cv_lib_db3_cxx_Dbopen,
[AC_LANG_SAVE
AC_LANG([C++])
djm_save_LIBS="$LIBS"
LIBS="$LIBS -ldb3 -ldb3_cxx"
AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <db_cxx.h>]], [[Db *d = new Db(NULL, 0);
d->open(NULL, NULL, DB_BTREE, DB_CREATE, 0);]])],[djm_cv_lib_db3_cxx_Dbopen=yes],[djm_cv_lib_db3_cxx_Dbopen=no])
LIBS="$djm_save_LIBS"
AC_LANG_RESTORE])

if test $djm_cv_lib_db3_cxx_Dbopen = yes; then
	LIBS="$LIBS -ldb3 -ldb3_cxx"
else

dnl Berkeley DB 4.0 installed as libdb4 (as on FreeBSD).
AC_CACHE_CHECK([for Db::open in -ldb4_cxx], djm_cv_lib_db4_cxx_Dbopen,
[AC_LANG_SAVE
AC_LANG([C++])
djm_save_LIBS="$LIBS"
LIBS="$LIBS -ldb4 -ldb4_cxx"
AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <db_cxx.h>]], [[Db *d = new Db(NULL, 0);
d->open(NULL, NULL, DB_BTREE, DB_CREATE, 0);]])],[djm_cv_lib_db4_cxx_Dbopen=yes],[djm_cv_lib_db4_cxx_Dbopen=no])
LIBS="$djm_save_LIBS"
AC_LANG_RESTORE])

if test $djm_cv_lib_db4_cxx_Dbopen = yes; then
	LIBS="$LIBS -ldb4 -ldb4_cxx"
else

dnl Berkeley DB 4.1+ installed as libdb4 (as on FreeBSD).
AC_CACHE_CHECK([for Db::open 4.1+ in -ldb4_cxx], djm_cv_lib_db41_cxx_Dbopen,
[AC_LANG_SAVE
AC_LANG([C++])
djm_save_LIBS="$LIBS"
LIBS="$LIBS -ldb4 -ldb4_cxx"
AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <db_cxx.h>]], [[Db *d = new Db(NULL, 0);
d->open(NULL, NULL, NULL, DB_BTREE, DB_CREATE, 0);]])],[djm_cv_lib_db41_cxx_Dbopen=yes],[djm_cv_lib_db41_cxx_Dbopen=no])
LIBS="$djm_save_LIBS"
AC_LANG_RESTORE])

if test $djm_cv_lib_db41_cxx_Dbopen = yes; then
	LIBS="$LIBS -ldb4 -ldb4_cxx"
else

dnl Berkeley DB 4.1-6.x installed as libdb.
AC_CACHE_CHECK([for Db::open 4.1-6.x in -ldb_cxx], djm_cv_lib_db_cxx_Dbopen_5,
[AC_LANG_SAVE
AC_LANG([C++])
djm_save_LIBS="$LIBS"
LIBS="$LIBS -ldb -ldb_cxx"
AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <db_cxx.h>]], [[Db *d = new Db(NULL, 0);
d->open(NULL, NULL, NULL, DB_BTREE, DB_CREATE, 0);]])],[djm_cv_lib_db_cxx_Dbopen_5=yes],[djm_cv_lib_db_cxx_Dbopen_5=no])
LIBS="$djm_save_LIBS"
AC_LANG_RESTORE])

if test $djm_cv_lib_db_cxx_Dbopen_5 = yes; then
	LIBS="$LIBS -ldb -ldb_cxx"
else

dnl Berkeley DB 5.x installed as libdb5.
AC_CACHE_CHECK([for Db::open in -ldb5_cxx], djm_cv_lib_db5_cxx_Dbopen,
[AC_LANG_SAVE
AC_LANG([C++])
djm_save_LIBS="$LIBS"
LIBS="$LIBS -ldb5 -ldb5_cxx"
AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <db_cxx.h>]], [[Db *d = new Db(NULL, 0);
d->open(NULL, NULL, NULL, DB_BTREE, DB_CREATE, 0);]])],[djm_cv_lib_db5_cxx_Dbopen=yes],[djm_cv_lib_db5_cxx_Dbopen=no])
LIBS="$djm_save_LIBS"
AC_LANG_RESTORE])

if test $djm_cv_lib_db5_cxx_Dbopen = yes; then
	LIBS="$LIBS -ldb5 -ldb5_cxx"
else

dnl Berkeley DB 6.x installed as libdb6.
AC_CACHE_CHECK([for Db::open in -ldb6_cxx], djm_cv_lib_db6_cxx_Dbopen,
[AC_LANG_SAVE
AC_LANG([C++])
djm_save_LIBS="$LIBS"
LIBS="$LIBS -ldb6 -ldb6_cxx"
AC_LINK_IFELSE([AC_LANG_PROGRAM([[#include <db_cxx.h>]], [[Db *d = new Db(NULL, 0);
d->open(NULL, NULL, NULL, DB_BTREE, DB_CREATE, 0);]])],[djm_cv_lib_db6_cxx_Dbopen=yes],[djm_cv_lib_db6_cxx_Dbopen=no])
LIBS="$djm_save_LIBS"
AC_LANG_RESTORE])

if test $djm_cv_lib_db6_cxx_Dbopen = yes; then
	LIBS="$LIBS -ldb6 -ldb6_cxx"
else


	AC_MSG_ERROR([Berkeley DB library 2.x-6.x configured with --enable-cxx is required])
fi
fi
fi
fi
fi
fi
fi
fi])

DJM_LIB_DB_CXX

AC_CONFIG_FILES([Makefile dns-terror/Makefile scripts/Makefile
          scripts/btree-dump scripts/convert-ip-db scripts/expire-ip-db
          scripts/rebuild-ip-db scripts/reresolve scripts/make-report])
AC_OUTPUT
