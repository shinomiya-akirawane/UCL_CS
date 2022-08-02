import java.util.*;
public class Main {
    public static void main(String[] args) {    // 'String'[] args is a parameter of main
        ArrayList <String>l = new ArrayList<String>();
        l.add("a");
        l.add("b");
        l.add("c");
        VoteCounter c = new VoteCounter(l);
        try{
        c.voteFor("a");
        System.out.println(c.getVoteCount("a"));
        }
        catch (VoteException s){
            s.print();
        }
    }
}
class VoteCounter{   
    Hashtable<String,Integer> counter = new Hashtable<String,Integer>();
    public VoteCounter(ArrayList<String> list){
        for (String opt : list){
            counter.put(opt,0);
        }
    }
    public void voteFor(String opt) throws VoteException{
        if (counter.replace(opt,counter.get(opt)+1) == null){
            throw new VoteException();
        }
    }
    public int getVoteCount(String opt)throws VoteException{
        if(counter.get(opt) == null){
            throw new VoteException();
        }
        else{
        return counter.get(opt);
        }
    }
}

class VoteException extends Exception{
    String warning = "invalid opt name!";
    public void print(){
        System.out.println(warning);
    }
}
