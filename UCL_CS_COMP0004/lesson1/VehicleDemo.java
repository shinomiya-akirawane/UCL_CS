import java.util.Hashtable;

import javax.management.monitor.GaugeMonitor;

import java.util.ArrayList;
class Vehicle {
    int passengers;
    int fuelcap;
    public Vehicle(int passenger, int fuelcap){
        System.out.println("build a vehicle class");
    }
    public double getSpeed(){
        return passengers/1;
    } 
}

class Manager extends Employee{
    int bonus;
    public Manager(String name,String department,int pay,int bonus){
        super(name,department,pay);
        this.bonus = bonus;
    }

    public int getMonthlyPay(){
        return this.pay+this.bonus;
    }
}

class ExecutiveTeam{
    Hashtable<String,Manager> team = new Hashtable<String,Manager>();
    public ExecutiveTeam(){
        
    }
    public void add(Manager manager){
        team.put(manager.name, manager);
    }
    public void remove(String name){
        team.remove(name);
    }
}

class Employee{
    String name;
    String department;
    int pay;
    public Employee(String name,String department,int pay){
        this.name = name;
        this.department = department;
        this.pay = pay;
    }
    public String getName(){
        return this.name;
    }
    public String getDepartment(){
        return this.department;
    }
    public int getMonthlyPay(){
        return this.pay;
    }
}
class Worker extends Employee{
    public Worker(String name,String department,int pay){
        super(name,department,pay);
    }
    private int cal(int n){
        int ans = 1;
        for (int i=0;i<=n;i++){
            ans = ans*2;
        }
        return ans;
    }
}

class Company{
    String name;
    Hashtable <String,Manager> allManager = new Hashtable<String,Manager>();
    Hashtable <String,Worker> allWorker = new Hashtable<String,Worker>();
    public Company(String name){
        this.name = name;
    }
    public void addWorker(String name,String department,int pay){
        Worker newWorker = new Worker(name, department, pay);
        allWorker.put(name, newWorker);
    }
    public void addManager(String name,String department,int pay,int bonus){
        Manager newManager = new Manager(name, department, pay, bonus);
        allManager.put(name, newManager);
    }
    public void addToExecutiveTeam(Manager manager){
        ExecutiveTeam team = new ExecutiveTeam();
        team.add(manager);
    }
    public int getTotalPayPerMonth(){
        int managerPay = 0;
        int workerPay = 0;
        for(String name:allManager.keySet()){
            managerPay += allManager.get(name).getMonthlyPay();
        }
        for(String name:allWorker.keySet()){
            workerPay += allWorker.get(name).getMonthlyPay();
        }
        return managerPay+workerPay;
    }
    private ArrayList<Integer> complete(ArrayList<Integer> list){
        ArrayList<Integer> res = new ArrayList<Integer>();
        for (int i =0;i<=100;i++){
            if (!list.contains(i)){
                res.add(i);
            }
        }
        return res;
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

public class VehicleDemo {
    public static void main (String args []) {
        Vehicle minivan = new Vehicle(10,100);
        minivan.passengers = 2;
        minivan.fuelcap = 10;
        System.out.println(minivan.getSpeed());
    }
}
