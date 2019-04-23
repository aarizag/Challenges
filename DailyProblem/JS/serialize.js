
class Node {
    constructor(val, left=null, right=null){
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function iterative_print(node){
    let stack = [node];
    while(stack.length > 0){
        let n = stack.pop();
        if (n.right != null)
            stack.push(n.right);
        if (n.left != null)
            stack.push(n.left);
        console.log(n.val)
    }
}

function serialize(node){
    if(node == null)
        return "null";
    return `${node.val},${serialize(node.left)},${serialize(node.right)}`
}

function deserialize(n_string){
    let split_str = n_string.split(",");

    function inner(){
        if(split_str == null)
            return null;
        let val = split_str.shift();
        let parent = null;
        if(val.localeCompare("null") !== 0)
            parent = Node(val, inner(), inner());
        return parent
    }

    return inner()
}