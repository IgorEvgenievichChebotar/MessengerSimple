#include <iostream>
using namespace std;

struct node {
	int value;
	node* left;
	node* right;
};

class btree {
public:
	btree();
	~btree();

	void insert(int key);
	node* search(int key);
	void destroy_tree();
	void inorder_print();
	void postorder_print();
	void preorder_print();

private:
	void destroy_tree(node* leaf);
	void insert(int key, node* leaf);
	node* search(int key, node* leaf);
	void inorder_print(node* leaf);
	void postorder_print(node* leaf);
	void preorder_print(node* leaf);

	node* root_;
};


btree::btree() : root_(nullptr)
{
}

btree::~btree() {
	destroy_tree();
}

void btree::destroy_tree(node* leaf) {
	if (leaf != nullptr) {
		destroy_tree(leaf->left);
		destroy_tree(leaf->right);
		delete leaf;
	}
}

void btree::insert(const int key, node* leaf) {

	if (key < leaf->value) {
		if (leaf->left != nullptr) {
			insert(key, leaf->left);
		}
		else {
			leaf->left = new node;
			leaf->left->value = key;
			leaf->left->left = nullptr;
			leaf->left->right = nullptr;
		}
	}
	else if (key >= leaf->value) {
		if (leaf->right != nullptr) {
			insert(key, leaf->right);
		}
		else {
			leaf->right = new node;
			leaf->right->value = key;
			leaf->right->right = nullptr;
			leaf->right->left = nullptr;
		}
	}

}

void btree::insert(const int key) {
	if (root_ != nullptr) {
		insert(key, root_);
	}
	else {
		root_ = new node;
		root_->value = key;
		root_->left = nullptr;
		root_->right = nullptr;
	}
}

node* btree::search(const int key, node* leaf) {
	if (leaf != nullptr) {
		if (key == leaf->value) {
			return leaf;
		}
		if (key < leaf->value) {
			return search(key, leaf->left);
		}
		else {
			return search(key, leaf->right);
		}
	}
	else {
		return nullptr;
	}
}

node* btree::search(const int key) {
	return search(key, root_);
}

void btree::destroy_tree() {
	destroy_tree(root_);
}

void btree::inorder_print() {
	inorder_print(root_);
	cout << "\n";
}

void btree::inorder_print(node* leaf) {
	if (leaf != nullptr) {
		inorder_print(leaf->left);
		cout << leaf->value << ",";
		inorder_print(leaf->right);
	}
}

void btree::postorder_print() {
	postorder_print(root_);
	cout << "\n";
}

void btree::postorder_print(node* leaf) {
	if (leaf != nullptr) {
		inorder_print(leaf->left);
		inorder_print(leaf->right);
		cout << leaf->value << ",";
	}
}

void btree::preorder_print() {
	preorder_print(root_);
	cout << "\n";
}

void btree::preorder_print(node* leaf) {
	if (leaf != nullptr) {
		cout << leaf->value << ",";
		inorder_print(leaf->left);
		inorder_print(leaf->right);
	}
}

int main() {

	//btree tree;
	auto* tree = new btree();

	tree->insert(10);
	tree->insert(6);
	tree->insert(14);
	tree->insert(5);
	tree->insert(8);
	tree->insert(11);
	tree->insert(18);

	tree->preorder_print();
	tree->inorder_print();
	tree->postorder_print();

	delete tree;

}