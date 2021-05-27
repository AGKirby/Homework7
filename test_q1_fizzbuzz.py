import unittest
import q1_fizzbuzz

class testCaseAdd(unittest.TestCase):
    def test_fizzbuzz1(self): #check that the function prints numbers 1 to 100
        expected = "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31\n32\n33\n34\n35\n36\n37\n38\n39\n40\n41\n42\n43\n44\n45\n46\n47\n48\n49\n50\n51\n52\n53\n54\n55\n56\n57\n58\n59\n60\n61\n62\n63\n64\n65\n66\n67\n68\n69\n70\n71\n72\n73\n74\n75\n76\n77\n78\n79\n80\n81\n82\n83\n84\n85\n86\n87\n88\n89\n90\n91\n92\n93\n94\n95\n96\n97\n98\n99\n100\n"
        result = q1_fizzbuzz.fizzbuzz()
        self.assertEqual(result, expected)

    def test_fizzbuzz2(self): #check that numbers divisible by 3 printed as "Fizz"
        expected = "1\n2\nFizz\n4\n5\nFizz\n7\n8\nFizz\n10\n11\nFizz\n13\n14\nFizz\n16\n17\nFizz\n19\n20\nFizz\n22\n23\nFizz\n25\n26\nFizz\n28\n29\nFizz\n31\n32\nFizz\n34\n35\nFizz\n37\n38\nFizz\n40\n41\nFizz\n43\n44\nFizz\n46\n47\nFizz\n49\n50\nFizz\n52\n53\nFizz\n55\n56\nFizz\n58\n59\nFizz\n61\n62\nFizz\n64\n65\nFizz\n67\n68\nFizz\n70\n71\nFizz\n73\n74\nFizz\n76\n77\nFizz\n79\n80\nFizz\n82\n83\nFizz\n85\n86\nFizz\n88\n89\nFizz\n91\n92\nFizz\n94\n95\nFizz\n97\n98\nFizz\n100\n"
        result = q1_fizzbuzz.fizzbuzz()
        self.assertEqual(result, expected)

    def test_fizzbuzz3(self): #check that numbers divisible by 3 printed as "Fizz" and numbers divisible by 5 printed as "Buzz"
        expected = "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz\n"
        result = q1_fizzbuzz.fizzbuzz()
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)