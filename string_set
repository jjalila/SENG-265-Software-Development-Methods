#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "string_set.h"

using namespace std;

const int debug = 0;

string_set::string_set() {
	iterator_index=0;
	
	int i;
	for (i=0;i<HASH_TABLE_SIZE;i++) {
	  hash_table[i]=NULL;
	}
	iterator_node=hash_table[0];
}

void string_set::add(const char *s) {
	if (contains(s)) {
	  throw duplicate_exception();
	}
	int hash= hash_function(s);
	node* snode,*curr;
	try {
	  snode=new node;
	}catch (int e) {
	  throw memory_exception();
	}
	int len=strlen(s);
	snode->s=new char[len+1];
	int i;
	for (i=0;s[i]!='\0';i++) {
	  snode->s[i]=s[i];
	}
	snode->s[len]='\0';
	snode->next=NULL;
	curr=hash_table[hash];
	if (!curr) {
	  hash_table[hash]=snode;
	}else {
	  //back of list (head)
	  snode->next=curr;
	  hash_table[hash]=snode;
	  
	  /* front of list (tail)
	  for (;curr->next;curr=curr->next);
	  curr->next=snode;
	  */
	}
	reset();
}

void string_set::remove(const char *s) {
	int h;
	h=hash_function(s);
	node * curr,* prev;
	prev= NULL;
	for (curr=hash_table[h];curr;prev=curr,curr=curr->next) {
	  if (!strcmp(s,curr->s)) {
	    if (!prev) {
	      hash_table[h]=curr->next;
	    }else {
	      prev->next=curr->next;
	    }
	    delete [] curr->s;
	    delete curr;
	    reset();
	    return;
	  }
	  
	}
	throw not_found_exception();
}

int string_set::contains(const char *s) {
	int h;
	if (debug) {
	  cout<< "s is " << s << endl;
	  cout<< "calling hash_function!"<< endl;
	}
	h=hash_function(s);
	if (debug) {
	  cout<< "s hash to "<< h << endl;
	}
	node * curr;
	curr=hash_table[h];
	for (;curr;curr=curr->next) {
	  if (!strcmp(s,curr->s)) {
	    return 1;
	  }
	}
	return 0;
}

void string_set::reset() {
	iterator_index=0;
	iterator_node=hash_table[0];
}

const char *string_set::next() {
	char *s;
	int l;
	if (debug) {
	  cout<< "Index: "<< iterator_index << endl;
	}
	while (!iterator_node && iterator_index+1<HASH_TABLE_SIZE) {
	  iterator_index++;
	  iterator_node=hash_table[iterator_index];
	}
	if (iterator_node && iterator_node->next) {
	  l=strlen(iterator_node->s);
	  s= new char[l+1];
	  strcpy(s,iterator_node->s);
	  iterator_node=iterator_node->next;
	  if (debug) {
	    cout << "has next "<< endl;
	    cout<< "Index: "<< iterator_index << endl;
	  }
	  return s;
	}
	if (iterator_node) {
	  l=strlen(iterator_node->s);
	  s= new char[l+1];
	  strcpy(s,iterator_node->s);
	  iterator_index++;
	  iterator_node=hash_table[iterator_index];
	  if (debug) {
	    cout << "has no next "<< endl;
	    cout<< "Index: "<< iterator_index << endl;
	  }
	  return s;
// 	  while (!iterator_node && iterator_index+1<HASH_TABLE_SIZE) {
// 	    iterator_index++;
// 	    iterator_node=hash_table[iterator_index];
// 	  }
	}
	  
	
	return NULL;
}

string_set::~string_set() {
	int i;
	node* curr;
	for(i=0;i<HASH_TABLE_SIZE;i++) {
	  curr=hash_table[i];
	  while (curr) {
	    hash_table[i]=curr->next;
	    delete [] curr->s;
	    delete [] curr;
	    curr=hash_table[i];
	  }
	}
}

int string_set::hash_function(const char *s) {
	int ans=0;
	char * cp;
	for (cp=(char *)s;*cp!='\0';cp++) {
	  ans +=(int)(*cp);
	}
	return ans % HASH_TABLE_SIZE; 
}
