//Exercise 1

def generateVerses(n: Int): List[String] = {
  (1 to n).reverse.map { i =>
   if (i == 1)
      "1 bottle of beer on the wall, 1 bottle of beer.\n" +
      "Take one down and pass it around, no more bottles of beer on the wall.\n"
    else
      i + " bottles of beer on the wall, " + i + " bottles of beer.\n" +
      "Take one down and pass it around, " + (i - 1) + " bottles of beer on the wall.\n"
  }.toList
}

def bottlesOfBeer(n: Int): Unit = {
  val verses = generateVerses(n)
  verses.foreach(println)
  
  println("No more bottles of beer on the wall, no more bottles of beer.")
  println("Go to the store and buy some more, 99 bottles of beer on the wall.")
}

bottlesOfBeer(99)

//Exercise 2

// Enumeration for Day
enum Day {
  case Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
  
  // Functions for Day
  def isWeekend: Boolean = this match {
    case Day.Saturday => true
    case Day.Sunday => true
    case Day.Monday | Day.Tuesday | Day.Wednesday | Day.Thursday | Day.Friday => false
  }

  def equal(that: Day): Boolean = this == that

  def previous: Day = this match {
    case Day.Monday => Day.Sunday
    case Day.Tuesday => Day.Monday
    case Day.Wednesday => Day.Tuesday
    case Day.Thursday => Day.Wednesday
    case Day.Friday => Day.Thursday
    case Day.Saturday => Day.Friday
    case Day.Sunday => Day.Saturday
  }

  def next: Day = this match {
    case Day.Monday => Day.Tuesday
    case Day.Tuesday => Day.Wednesday
    case Day.Wednesday => Day.Thursday
    case Day.Thursday => Day.Friday
    case Day.Friday => Day.Saturday
    case Day.Saturday => Day.Sunday
    case Day.Sunday => Day.Monday
  }
}

// Enumeration for Month
enum Month {
  case January, February, March, April, May, June, July, August, September, October, November, December

  // Function for Month
  def daysIn(year: Year): Int = this match {
    case Month.January => 31
    case Month.February if isLeapYear(year) => 29
    case Month.February => 28
    case Month.March => 31
    case Month.April => 30
    case Month.May => 31
    case Month.June => 30
    case Month.July => 31
    case Month.August => 31
    case Month.September => 30
    case Month.October => 31
    case Month.November => 30
    case Month.December => 31
  }
}

// Date Definition
type Year = Int
case class Date(day: Int, month: Month, year: Year)

// Functions for Date
def isLeapYear(year: Year): Boolean =
  (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)

def daysInMonth(month: Month, year: Year): Int = month.daysIn(year)

def yesterday(date: Date): Date = {
  val prevDay = if (date.day > 1) date.day - 1 else {
    val prevMonth = if (date.month == Month.January) Month.December else Month.values(date.month.ordinal - 1)
    val prevYear = if (date.month == Month.January) date.year - 1 else date.year
    daysInMonth(prevMonth, prevYear)
  }
  Date(prevDay, date.month, date.year)
}

def tomorrow(date: Date): Date = {
  val nextDay = if (date.day < daysInMonth(date.month, date.year)) date.day + 1 else {
    val nextMonth = if (date.month == Month.December) Month.January else Month.values(date.month.ordinal + 1)
    val nextYear = if (date.month == Month.December) date.year + 1 else date.year
    1
  }
  Date(nextDay, date.month, date.year)
}

// Function for Date Description
def description(date: Date): String = {
  val daySuffix = date.day % 10 match {
    case 1 if date.day != 11 => "st"
    case 2 if date.day != 12 => "nd"
    case 3 if date.day != 13 => "rd"
    case _ => "th"
  }
  
  val dayStr = date.day.toString + daySuffix
  dayStr + " of " + date.month.toString + ", " + date.year.toString
}

// Test
val testDate = Date(9, Month.March, 1973)
println(description(testDate))

//Exercise 3

// Function to calculate the product of f(i) from 0 to n
def productOfFunction(n: Int, f: Int => Int): Int = {
  (0 to n).map(f).sum
}

// Example function f(x) = x^2
def exampleFunction(x: Int): Int = x * x

val result = productOfFunction(5, exampleFunction)
println("Product of exampleFunction from 0 to 5: " + result)

//Exercise 4

// Function to convert an integer to its hexadecimal representation
def toHexaDecimal(n: Int): String = {
  if (n == 0) "0"
  else {
    val hexChars = "0123456789abcdef"
    def toHexHelper(num: Int, acc: String): String = {
      if (num == 0) acc
      else {
        val remainder = num % 16
        toHexHelper(num / 16, s"${hexChars.charAt(remainder)}$acc")
      }
    }
    toHexHelper(n, "")
  }
}

// Helper function to convert a single hexadecimal character to its integer value
def charToDecimal(c: Char): Option[Int] = {
  val hexChars = "0123456789abcdef"
  hexChars.indexOf(c.toLower) match {
    case -1 => None
    case index => Some(index)
  }
}

// Function to convert a hexadecimal string to its integer value
def fromHexadecimal(hex: String): (Int, Boolean) = {
  hex.foldLeft((0, true)) { case ((result, success), c) =>
    charToDecimal(c) match {
      case Some(value) => (result * 16 + value, success)
      case None => (result, false)
    }
  }
}

// Test
val number = 932
val hexString = toHexaDecimal(number)
println(s"The hexadecimal representation of $number is: $hexString")

val hex = "3a4"
val (convertedNumber, isSuccess) = fromHexadecimal(hex)
if (isSuccess) println(s"The decimal value of $hex is: $convertedNumber")
else println(s"Conversion from hexadecimal to decimal failed for $hex")
