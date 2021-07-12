clear all
clc
prompt = {'Enter the interval start :','Enter the interval end:','Enter the function :'};
data = inputdlg(prompt,'Bisection Method');
a=str2num(data{1});
b=str2num(data{2});
f=str2num(data{3});
d='@(x)';
f=str2func( strcat(d,data{3}));
j=0;
list = {'No. of itirations','Max. error bound'};
[indx,tf] = listdlg('ListString',list);
switch indx
    case 1
       prompt = {'Enter the NO. of itirations :'};
       data = inputdlg(prompt,'NO. of itirations');
       n=str2num(data{1});
      
    case 2
       prompt = {'Enter the Max. error bound:'};
       data = inputdlg(prompt,'Max. error bound');
       error=str2num(data{1});  
     n=log2((b-a)./error);
end 
 
while j<n
  x=(a+b)./2; 
  if f(a)*f(x)>0
      a=x;
  else
      b=x;
  end 
  j=j+1;
end 
msgbox(sprintf('x is equivalent to :%f',x));

    
