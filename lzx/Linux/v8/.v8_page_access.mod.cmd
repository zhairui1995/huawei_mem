savedcmd_v8_page_access.mod := printf '%s\n'   v8_page_access.o | awk '!x[$$0]++ { print("./"$$0) }' > v8_page_access.mod
