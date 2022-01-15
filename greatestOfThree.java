import java.util.Scanner; 
public class Main {
  static void greatestOfThree(int a, int b, int c) {
    if(a>=b && a>=c)  
System.out.println("The largest Number is: "+a);  
//comparing b with a and b with c  
//if both conditions are true, prints b  
else if (b>=a && b>=c)  
System.out.println("The largest Number is: "+b);  
else  
//prints c if the above conditions are false  
System.out.println("The largest Number is: "+c);
  }

  public static void main(String[] args) {
    int x,y,z; 
//object of the Scanner class  
Scanner sc = new Scanner(System.in);
System.out.println("Enter the first number: ");  
x = sc.nextInt();  
System.out.println("Enter the second number: ");  
y = sc.nextInt();  
System.out.println("Enter the third number: ");  
z = sc.nextInt(); 
greatestOfThree(x,y,z);
  
  }
}
