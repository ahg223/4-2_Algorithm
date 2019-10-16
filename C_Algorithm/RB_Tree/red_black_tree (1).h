#ifdef DMALLOC
#include <dmalloc.h>
#endif
#include"misc.h"
#include"stack.h"




#define DEBUG_ASSERT 1

typedef struct rb_red_blk_node {
  void* key;
  void* info;
  int red;
  struct rb_red_blk_node* left;
  struct rb_red_blk_node* right;
  struct rb_red_blk_node* parent;
} rb_red_blk_node;




typedef struct rb_red_blk_tree {
  int (*Compare)(const void* a, const void* b); 
  void (*DestroyKey)(void* a);
  void (*DestroyInfo)(void* a);
  void (*PrintKey)(const void* a);
  void (*PrintInfo)(void* a);
    
  rb_red_blk_node* root;             
  rb_red_blk_node* nil;              
} rb_red_blk_tree;

rb_red_blk_tree* RBTreeCreate(int  (*CompFunc)(const void*, const void*),
			     void (*DestFunc)(void*), 
			     void (*InfoDestFunc)(void*), 
			     void (*PrintFunc)(const void*),
			     void (*PrintInfo)(void*));
rb_red_blk_node * RBTreeInsert(rb_red_blk_tree*, void* key, void* info);
void RBTreePrint(rb_red_blk_tree*);
void RBDelete(rb_red_blk_tree* , rb_red_blk_node* );
void RBTreeDestroy(rb_red_blk_tree*);
rb_red_blk_node* TreePredecessor(rb_red_blk_tree*,rb_red_blk_node*);
rb_red_blk_node* TreeSuccessor(rb_red_blk_tree*,rb_red_blk_node*);
rb_red_blk_node* RBExactQuery(rb_red_blk_tree*, void*);
stk_stack * RBEnumerate(rb_red_blk_tree* tree,void* low, void* high);
void NullFunction(void*);
