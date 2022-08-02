import java.util.*;
class Buckets{
    public int min;
    public int max;
    ArrayList<ArrayList<Integer>> buckets = new ArrayList<ArrayList<Integer>>();
    public Buckets(int min,int max){
        for (int i = min;i<=max;i+=2){
            buckets.add(new ArrayList<Integer>()); 
        }
        this.min = min;
        this.max = max;
    }
    public void fillBucket(int n){
        int index = (n-this.min)/2;
        this.buckets.get(index).add(n);
        Collections.sort(this.buckets.get(index));
    }
    public ArrayList<Integer> getAllNums(){
        ArrayList<Integer> ans = new ArrayList<Integer>();
        for(ArrayList<Integer> bucket:this.buckets){
            for(int num:bucket){
                ans.add(num);
            }
        }
        return ans;
    }
}
public class BucketSort {
    public static void main(String[] args) { 
        int[] list = {3,3,6,5,2,1,7};
        Buckets buckets = new Buckets(1, 7);
        for(int num:list){
            buckets.fillBucket(num);
        }
        ArrayList<Integer> ans = buckets.getAllNums();
        System.out.println(ans);
    }
}
