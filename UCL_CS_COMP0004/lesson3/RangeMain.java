import java.util.*;
class Range {
    private int lower;
    private int upper;
    private ArrayList list = new ArrayList();
    public Range(int lower, int upper){
        this.lower = lower;
        this.upper = upper;
        for(int i=lower;i<=upper;i++)
            this.list.add(i);
    }
    public int getLower() {
        return lower;
    }
    public int getUpper() {
        return upper;
    }
    public boolean contains(int n) {
        if(list.size() == 0)
            return false;
        if(list.contains(n))
            return true;
        return false;
    }
    public ArrayList getValues(){
        return list;
    }
}
public class RangeMain {
    public static int r(){
        Scanner s = new Scanner(System.in);
        if(s.hasNextInt())
            return s.nextInt();
        else
            return 0;
    }
    public static void main(String args[]){
        int l,u;
        l = r();
        u = r();
        Range range = new Range(l,u);
    }
}
