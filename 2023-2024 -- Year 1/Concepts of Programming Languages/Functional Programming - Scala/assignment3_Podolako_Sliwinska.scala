val listOfTenNumbs = List(1,2,3,4,5,6,7,8,9,10)

//----------Ex1----------
def oddSquare(listOfNumbs: List[Int]): List[Int] = {
  listOfNumbs.map { x =>
    if (x % 2 != 0 ) x * x
    else x
  }
}
//----------Res1----------
println("Ex 1")
println(oddSquare(listOfTenNumbs)) //output: List(1, 2, 9, 4, 25, 6, 49, 8, 81, 10)

//----------Ex2----------
def oddIndexSquare(listOfNumbs: List[Int]): List[Int] = {
  listOfNumbs.map { i =>
    if (listOfNumbs.indexOf(i) % 2 != 0 ) i * i
    else i
  }
}
//----------Res2----------
println("Ex 2")
println(oddIndexSquare(listOfTenNumbs)) //output: List(1, 4, 3, 16, 5, 36, 7, 64, 9, 100)

//----------Ex3----------
def fizzbuz (m:Int, n:Int) (xs:List[Int]): (List[Int], List[Int], List[Int]) = {
  val divisibleByM = xs.filter(q => (q % m == 0))
  val divisibleByN = xs.filter(q => (q % n == 0) && (q % m != 0))
  val rest = xs.filter(q => (q % n != 0) && (q % m != 0))
  (divisibleByM, divisibleByN, rest)
}
//----------Res3----------
println("Ex 3")
println(fizzbuz(2, 3)(listOfTenNumbs)) //output: (List(2, 4, 6, 8, 10),List(3, 9),List(1, 5, 7))

//----------Ex4----------
def insertAt[A] (k:Int, elem:A, xs:List[A]): List[A] = {
  if (k < 0 || k >= (xs.length+1)) //base case if k is inacceptable (we can add new last el)
    xs 
  else { 
    val (before, after) = xs.splitAt(k) 
    before ++ (elem :: after) 
  } 
}
def removeAt[A] (k:Int, xs:List[A]): List[A] = {
  if (k < 0 || k >= xs.length) //base case if k is inacceptable
    xs 
  else { 
    val (before, after) = xs.splitAt(k) 
    before ++ after.tail 
  }  
}
//----------Res4----------
println("Ex 4")
println(insertAt(1, 222, listOfTenNumbs)) // test random place new el
println(insertAt(10, 11, listOfTenNumbs)) //test new last el
println(insertAt(0, 111, listOfTenNumbs)) //test new 1st el
println(insertAt(-1, 11, listOfTenNumbs)) //base case test

println(removeAt(5, listOfTenNumbs)) // test random place remove el
println(removeAt(9, listOfTenNumbs)) //test remove last el
println(removeAt(0, listOfTenNumbs)) //test remove 1st el
println(removeAt(10, listOfTenNumbs)) //base case test
/* Output:
List(1, 222, 2, 3, 4, 5, 6, 7, 8, 9, 10)
List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
List(111, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

List(1, 2, 3, 4, 5, 7, 8, 9, 10)
List(1, 2, 3, 4, 5, 6, 7, 8, 9)
List(2, 3, 4, 5, 6, 7, 8, 9, 10)
List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
*/

val listOfDuplicateNumbs = List(1,2,2,3,4,5,6,3,7,8,9,10)
//----------Ex5----------
def duplicates[A] (list:List[A]): Boolean = list match {
  case Nil => false
  case head :: tail => tail.contains(head) || duplicates(tail)
}
//----------Res5----------
println("Ex 5")
println(duplicates(listOfTenNumbs)) //output: false
println(duplicates(listOfDuplicateNumbs)) //output: true
