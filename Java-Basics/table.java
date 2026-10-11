import java.util.Scanner;
public class table{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the table:");
        int n=sc.nextInt();
        System.out.println(n+"th"+" Table is :");
        for(int i=1;i<=10;i++){
            System.out.println(n+" X "+ i +" = "+i*n);
        }
        System.out.print("this is the table of "+n);
    }
}