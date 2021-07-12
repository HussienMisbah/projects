
prompt = {'Enter X points :','Enter Y points:'};
data = inputdlg(prompt,'specify points in matrix form',[1 90]);
x=str2num(data{1});
y=str2num(data{2});
n=length(x);
Y=1./y;
X=1./x;

%Growth Model
M=[n     sum(X);sum(X) sum(X.^2)];
B=[sum(Y) ; sum(X.*Y) ];
co=M\B; 
a0=co(1);
a1=co(2);
ymean=sum(Y)/n;
St=sum((Y-ymean).^2);
Sr=sum((Y-a0-a1.*X).^2);
r=sqrt((St-Sr)/St); %to print latter
plot(x,y,'.');
grid on;
hold on;
a=(1./a0);
b=a1.*a;
xdash=linspace(min(x),max(x));
ydash=(a.*xdash)./(b+xdash);
plot(xdash,ydash)
title('Growth Model');
msgbox(sprintf('      Growth Model results       \na0=%f\na1=%f\ny=(%fx)/(%f+x)\n\ncorrelation coefficient is %f',a0,a1,a,b,r));
