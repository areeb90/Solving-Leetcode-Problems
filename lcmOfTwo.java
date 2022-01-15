
import java.util.Scanner; 
public class Main {
    static void LCMM (int x, int y){
    int gcd = 1;
    int temp, lcm;
    if (x > y) {
      temp = x;
      x = y;
      y = temp;
    }
    for(int i = 1; i < (x+1); i++) {
      if (x%i == 0 && y%i == 0)
        gcd = i;
    }
    lcm = (x*y)/gcd;
    System.out.println("LCM of "+ x +" and "+ y +" is: "+ lcm);
    }
  public static void main(String[] args) {
int x,y; 
//object of the Scanner class  
Scanner sc = new Scanner(System.in);
System.out.println("Enter the first number: ");  
x = sc.nextInt();  
System.out.println("Enter the second number: ");  
y = sc.nextInt();  
 
LCMM(x,y);
  }
}
