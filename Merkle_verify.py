from merkletools import MerkleTools


mt = MerkleTools()

mt.add_leaf("tierion", True)
mt.add_leaf(["bitcoin", "blockchain"], True)

mt.make_tree()

print mt.get_leaf_count();

print "root:", mt.get_merkle_root()  # root: '777765f15d171871b00034ee55e48ffdf76afbc44ed0bcff5c82f31351d333c2ed1'

print mt.get_proof(1)  # [{left: '2da7240f6c88536be72abe9f04e454c6478ee29709fc3729ddfb942f804fbf08'},
                       #  {right: 'ef7797e13d3a75526946a3bcf00daec9fc9c9c4d51ddc7cc5df888f74dd434d1'}] 

print mt.validate_proof(mt.get_proof(1), mt.get_leaf(1), mt.get_merkle_root()) 