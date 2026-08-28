//-------------------EX 1-------------------

def exponent(arg: Int, exp: Int): Int = {
  if (exp == 0) 1
  else arg * exponent(arg, exp - 1)
}

val resultExponent = exponent(5, 7)
println(resultExponent)

//-------------------EX 2-------------------

def getLastChar(otherString: String): Char = {
  otherString.charAt(otherString.length - 1)
}

val string2 = "Hello"
val lastCharacter = getLastChar(string2)
println(lastCharacter)

//-------------------EX 3-------------------

def removeDuplicate(string: String): String = {
  if (string.isEmpty) ""
  else if (string.tail.contains(string.head)) removeDuplicate(string.tail)
  else string.head.toString + removeDuplicate(string.tail)
}

val string3 = "Hello!"
val uniqueString = removeDuplicate(string3)
println(uniqueString)

//-------------------EX 4-------------------

def romanNumerals(integer: Int): String = {
  val values = Array(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
  val numerals = Array("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")

  def toRoman(num: Int, result: String = ""): String = {
    if (num == 0) result
    else {
      val index = values.indexWhere(v => v <= num)
      toRoman(num - values(index), result + numerals(index))
    }
  }

  toRoman(integer)
}

val resultRoman = romanNumerals(1464)
println(resultRoman)
