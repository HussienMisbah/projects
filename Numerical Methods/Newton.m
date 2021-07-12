
clc
syms 'x';
prompt = {'Enter the equation: ','Enter the initial guess: ','Enter number of steps:','Enter tollerance:'};
data = inputdlg(prompt,'enter inputs',[1 50]);
fun=str2num(data{1});
x0=str2num(data{2});
N=str2num(data{3});
error=str2num(data{4});
step = 1;
% Finding derivate of given function
df = diff(fun,x);

% Finding Functional Value
fa = eval(subs(fun,x,x0));

while abs(fa)> error
    fa = eval(subs(fun,x,x0));
    dfa = eval(subs(df,x,x0));
    if dfa == 0
        disp('Division by zero.');
        break;
    end   
    z = x0 - fa/dfa;
    fprintf('step=%d\ta=%f\tf(a)=%f\n',step,x0,fa);
    x0 = z;
    
    if step>N
       disp('Not convergent'); 
       break;
    end    
  step=step+1;
end
    
fprintf('Root is %f\n', x0);
msgbox(sprintf('x is equivalent to :%f',x0));

