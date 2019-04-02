class MyHashSet {

    /** Initialize your data structure here. */
    private Set<Integer> set;
    public MyHashSet() {
       this.set = new TreeSet<>();
    }
    
    public void add(int key) {
        this.set.add(key);
    }
    
    public void remove(int key) {
        this.set.remove(key);   
    }
    
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        return this.set.contains(key);
    }
}