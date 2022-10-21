function removeChar() {
  str=$1
  echo ${str:1:-1}
}
removeChar $1