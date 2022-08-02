import java.util.*;

class Bubble{
    int[] list;
    public Bubble(int[] list){
        this.list = list;
    } 
    public int[] sort(){
        for (int i =0;i<this.list.length-1;i++){
            for (int j=0;j<this.list.length-1-i;j++){
                if(list[j]>list[j+1]){
                    int temp = list[j];
                    list[j] = list[j+1];
                    list[j+1] = temp;
                }
            }
        }
        return list;
    }
}
public class BubbleSort{
    public static void main(String[] args) { 
        int[] list = {3,3,6,5,2,1,7};
        Bubble bubble = new Bubble(list);
        int [] ans = bubble.sort();
        for(int num:ans){
            System.out.println(num);
        }
    }
}