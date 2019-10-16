#include "red_black_tree.h"



rb_red_blk_tree* RBTreeCreate( int (*CompFunc) (const void*,const void*),
			      void (*DestFunc) (void*),
			      void (*InfoDestFunc) (void*),
			      void (*PrintFunc) (const void*),
			      void (*PrintInfo)(void*)) {
  rb_red_blk_tree* newTree;
  rb_red_blk_node* temp;

  newTree=(rb_red_blk_tree*) SafeMalloc(sizeof(rb_red_blk_tree));
  newTree->Compare=  CompFunc;
  newTree->DestroyKey= DestFunc;
  newTree->PrintKey= PrintFunc;
  newTree->PrintInfo= PrintInfo;
  newTree->DestroyInfo= InfoDestFunc;

    
    
    
  temp=newTree->nil= (rb_red_blk_node*) SafeMalloc(sizeof(rb_red_blk_node));
  temp->parent=temp->left=temp->right=temp;
  temp->red=0;
  temp->key=0;
  temp=newTree->root= (rb_red_blk_node*) SafeMalloc(sizeof(rb_red_blk_node));
  temp->parent=temp->left=temp->right=newTree->nil;
  temp->key=0;
  temp->red=0;
  return(newTree);
}




void LeftRotate(rb_red_blk_tree* tree, rb_red_blk_node* x) {
  rb_red_blk_node* y;
  rb_red_blk_node* nil=tree->nil;

    
  y=x->right;
  x->right=y->left;

  if (y->left != nil) y->left->parent=x;
  
  y->parent=x->parent;   

    
  if( x == x->parent->left) {
    x->parent->left=y;
  } else {
    x->parent->right=y;
  }
  y->left=x;
  x->parent=y;

#ifdef DEBUG_ASSERT
  Assert(!tree->nil->red,"nil not red in LeftRotate");
#endif
}




void RightRotate(rb_red_blk_tree* tree, rb_red_blk_node* y) {
  rb_red_blk_node* x;
  rb_red_blk_node* nil=tree->nil;

    
  x=y->left;
  y->left=x->right;

  if (nil != x->right)  x->right->parent=y;
    
    
  x->parent=y->parent;
  if( y == y->parent->left) {
    y->parent->left=x;
  } else {
    y->parent->right=x;
  }
  x->right=y;
  y->parent=x;

#ifdef DEBUG_ASSERT
  Assert(!tree->nil->red,"nil not red in RightRotate");
#endif
}




void TreeInsertHelp(rb_red_blk_tree* tree, rb_red_blk_node* z) {
    
  rb_red_blk_node* x;
  rb_red_blk_node* y;
  rb_red_blk_node* nil=tree->nil;
  
  z->left=z->right=nil;
  y=tree->root;
  x=tree->root->left;
  while( x != nil) {
    y=x;
    if (1 == tree->Compare(x->key,z->key)) {
      x=x->left;
    } else {
      x=x->right;
    }
  }
  z->parent=y;
  if ( (y == tree->root) ||
       (1 == tree->Compare(y->key,z->key))) {
    y->left=z;
  } else {
    y->right=z;
  }

#ifdef DEBUG_ASSERT
  Assert(!tree->nil->red,"nil not red in TreeInsertHelp");
#endif
}




rb_red_blk_node * RBTreeInsert(rb_red_blk_tree* tree, void* key, void* info) {
  rb_red_blk_node * y;
  rb_red_blk_node * x;
  rb_red_blk_node * newNode;

  x=(rb_red_blk_node*) SafeMalloc(sizeof(rb_red_blk_node));
  x->key=key;
  x->info=info;

  TreeInsertHelp(tree,x);
  newNode=x;
  x->red=1;
  while(x->parent->red) {
    if (x->parent == x->parent->parent->left) {
      y=x->parent->parent->right;
      if (y->red) {
	x->parent->red=0;
	y->red=0;
	x->parent->parent->red=1;
	x=x->parent->parent;
      } else {
	if (x == x->parent->right) {
	  x=x->parent;
	  LeftRotate(tree,x);
	}
	x->parent->red=0;
	x->parent->parent->red=1;
	RightRotate(tree,x->parent->parent);
      } 
    } else {
      y=x->parent->parent->left;
      if (y->red) {
	x->parent->red=0;
	y->red=0;
	x->parent->parent->red=1;
	x=x->parent->parent;
      } else {
	if (x == x->parent->left) {
	  x=x->parent;
	  RightRotate(tree,x);
	}
	x->parent->red=0;
	x->parent->parent->red=1;
	LeftRotate(tree,x->parent->parent);
      } 
    }
  }
  tree->root->left->red=0;
  return(newNode);

#ifdef DEBUG_ASSERT
  Assert(!tree->nil->red,"nil not red in RBTreeInsert");
  Assert(!tree->root->red,"root not red in RBTreeInsert");
#endif
}


  
rb_red_blk_node* TreeSuccessor(rb_red_blk_tree* tree,rb_red_blk_node* x) { 
  rb_red_blk_node* y;
  rb_red_blk_node* nil=tree->nil;
  rb_red_blk_node* root=tree->root;

  if (nil != (y = x->right)) {
    while(y->left != nil) {
      y=y->left;
    }
    return(y);
  } else {
    y=x->parent;
    while(x == y->right) {
      x=y;
      y=y->parent;
    }
    if (y == root) return(nil);
    return(y);
  }
}



rb_red_blk_node* TreePredecessor(rb_red_blk_tree* tree, rb_red_blk_node* x) {
  rb_red_blk_node* y;
  rb_red_blk_node* nil=tree->nil;
  rb_red_blk_node* root=tree->root;

  if (nil != (y = x->left)) {
    while(y->right != nil) {
      y=y->right;
    }
    return(y);
  } else {
    y=x->parent;
    while(x == y->left) { 
      if (y == root) return(nil); 
      x=y;
      y=y->parent;
    }
    return(y);
  }
}



void InorderTreePrint(rb_red_blk_tree* tree, rb_red_blk_node* x) {
  rb_red_blk_node* nil=tree->nil;
  rb_red_blk_node* root=tree->root;
  if (x != tree->nil) {
    InorderTreePrint(tree,x->left);
    printf("info=");
    tree->PrintInfo(x->info);
    printf("  key="); 
    tree->PrintKey(x->key);
    printf("  l->key=");
    if( x->left == nil) printf("NULL"); else tree->PrintKey(x->left->key);
    printf("  r->key=");
    if( x->right == nil) printf("NULL"); else tree->PrintKey(x->right->key);
    printf("  p->key=");
    if( x->parent == root) printf("NULL"); else tree->PrintKey(x->parent->key);
    printf("  red=%i\n",x->red);
    InorderTreePrint(tree,x->right);
  }
}




void TreeDestHelper(rb_red_blk_tree* tree, rb_red_blk_node* x) {
  rb_red_blk_node* nil=tree->nil;
  if (x != nil) {
    TreeDestHelper(tree,x->left);
    TreeDestHelper(tree,x->right);
    tree->DestroyKey(x->key);
    tree->DestroyInfo(x->info);
    free(x);
  }
}




void RBTreeDestroy(rb_red_blk_tree* tree) {
  TreeDestHelper(tree,tree->root->left);
  free(tree->root);
  free(tree->nil);
  free(tree);
}




void RBTreePrint(rb_red_blk_tree* tree) {
  InorderTreePrint(tree,tree->root->left);
}




rb_red_blk_node* RBExactQuery(rb_red_blk_tree* tree, void* q) {
  rb_red_blk_node* x=tree->root->left;
  rb_red_blk_node* nil=tree->nil;
  int compVal;
  if (x == nil) return(0);
  compVal=tree->Compare(x->key,(int*) q);
  while(0 != compVal) {/*assignemnt*/
    if (1 == compVal) { /* x->key > q */
      x=x->left;
    } else {
      x=x->right;
    }
    if ( x == nil) return(0);
    compVal=tree->Compare(x->key,(int*) q);
  }
  return(x);
}




void RBDeleteFixUp(rb_red_blk_tree* tree, rb_red_blk_node* x) {
  rb_red_blk_node* root=tree->root->left;
  rb_red_blk_node* w;

  while( (!x->red) && (root != x)) {
    if (x == x->parent->left) {
      w=x->parent->right;
      if (w->red) {
	w->red=0;
	x->parent->red=1;
	LeftRotate(tree,x->parent);
	w=x->parent->right;
      }
      if ( (!w->right->red) && (!w->left->red) ) { 
	w->red=1;
	x=x->parent;
      } else {
	if (!w->right->red) {
	  w->left->red=0;
	  w->red=1;
	  RightRotate(tree,w);
	  w=x->parent->right;
	}
	w->red=x->parent->red;
	x->parent->red=0;
	w->right->red=0;
	LeftRotate(tree,x->parent);
	x=root;
      }
    } else {
      w=x->parent->left;
      if (w->red) {
	w->red=0;
	x->parent->red=1;
	RightRotate(tree,x->parent);
	w=x->parent->left;
      }
      if ( (!w->right->red) && (!w->left->red) ) { 
	w->red=1;
	x=x->parent;
      } else {
	if (!w->left->red) {
	  w->right->red=0;
	  w->red=1;
	  LeftRotate(tree,w);
	  w=x->parent->left;
	}
	w->red=x->parent->red;
	x->parent->red=0;
	w->left->red=0;
	RightRotate(tree,x->parent);
	x=root;
      }
    }
  }
  x->red=0;

#ifdef DEBUG_ASSERT
  Assert(!tree->nil->red,"nil not black in RBDeleteFixUp");
#endif
}





void RBDelete(rb_red_blk_tree* tree, rb_red_blk_node* z){
  rb_red_blk_node* y;
  rb_red_blk_node* x;
  rb_red_blk_node* nil=tree->nil;
  rb_red_blk_node* root=tree->root;

  y= ((z->left == nil) || (z->right == nil)) ? z : TreeSuccessor(tree,z);
  x= (y->left == nil) ? y->right : y->left;
  if (root == (x->parent = y->parent)) {
    root->left=x;
  } else {
    if (y == y->parent->left) {
      y->parent->left=x;
    } else {
      y->parent->right=x;
    }
  }
  if (y != z) {

#ifdef DEBUG_ASSERT
    Assert( (y!=tree->nil),"y is nil in RBDelete\n");
#endif
      

    if (!(y->red)) RBDeleteFixUp(tree,x);
  
    tree->DestroyKey(z->key);
    tree->DestroyInfo(z->info);
    y->left=z->left;
    y->right=z->right;
    y->parent=z->parent;
    y->red=z->red;
    z->left->parent=z->right->parent=y;
    if (z == z->parent->left) {
      z->parent->left=y; 
    } else {
      z->parent->right=y;
    }
    free(z); 
  } else {
    tree->DestroyKey(y->key);
    tree->DestroyInfo(y->info);
    if (!(y->red)) RBDeleteFixUp(tree,x);
    free(y);
  }
  
#ifdef DEBUG_ASSERT
  Assert(!tree->nil->red,"nil not black in RBDelete");
#endif
}




stk_stack* RBEnumerate(rb_red_blk_tree* tree, void* low, void* high) {
  stk_stack* enumResultStack;
  rb_red_blk_node* nil=tree->nil;
  rb_red_blk_node* x=tree->root->left;
  rb_red_blk_node* lastBest=nil;

  enumResultStack=StackCreate();
  while(nil != x) {
    if ( 1 == (tree->Compare(x->key,high)) ) { /* x->key > high */
      x=x->left;
    } else {
      lastBest=x;
      x=x->right;
    }
  }
  while ( (lastBest != nil) && (1 != tree->Compare(low,lastBest->key))) {
    StackPush(enumResultStack,lastBest);
    lastBest=TreePredecessor(tree,lastBest);
  }
  return(enumResultStack);
}
      
    
  
  



