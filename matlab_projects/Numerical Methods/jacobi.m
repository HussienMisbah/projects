clear all;
clc;
% ask the user to enter the coefficient matrix, the constant vector
% ,initial guess vector, number of iterations & tolerance %
prompt = {'Enter the coefficient matrix: ','Enter the constant vector: ','Enter the intial guess vector: ','Enter number of itirations:','Enter tollerance:'};
data = inputdlg(prompt,'enter inputs',[1 50]);
A=str2num(data{1});
B=str2num(data{2});
C=str2num(data{3});
n=str2num(data{4});
T=str2num(data{5});

% Check matrix size
[M,N] = size(A);
 if M~=N
     error('A should be a square matrix');
 end

% Check for diagonally dominant %
for m = 1:M
    row = abs(A(m,:));
    s = sum(row) - row(m);
    if row(m) <= s
        error('Matrix A should be diagonally dominant');
    end
end

% initial guess %
x = zeros(M,1);

% the main loop
for j = 1:n
    for i = 1:N
        x(i) = (B(i)/A(i,i))-(A(i,[1:i-1,i+1:M])*C([1:i-1,i+1:M]))/A(i,i);
    end
    fprintf('Iteration number: %d\n',j)
    x
    if abs(x-C)<T
        break
    end
  C = x;
end
