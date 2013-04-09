function varargout = integrateatron(varargin)
% INTEGRATEATRON M-file for integrateatron.fig
%      INTEGRATEATRON, by itself, creates a new INTEGRATEATRON or raises the existing
%      singleton*.
%
%      H = INTEGRATEATRON returns the handle to a new INTEGRATEATRON or the handle to
%      the existing singleton*.
%
%      INTEGRATEATRON('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in INTEGRATEATRON.M with the given input arguments.
%
%      INTEGRATEATRON('Property','Value',...) creates a new INTEGRATEATRON or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before integrateatron_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to integrateatron_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help integrateatron

% Last Modified by GUIDE v2.5 03-Mar-2013 13:52:33

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @integrateatron_OpeningFcn, ...
                   'gui_OutputFcn',  @integrateatron_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before integrateatron is made visible.
function integrateatron_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to integrateatron (see VARARGIN)

% Choose default command line output for integrateatron
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes integrateatron wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = integrateatron_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function inputFunction_Callback(hObject, eventdata, handles)
% hObject    handle to inputFunction (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of inputFunction as text
%        str2double(get(hObject,'String')) returns contents of inputFunction as a double
syms x;


% --- Executes during object creation, after setting all properties.
function inputFunction_CreateFcn(hObject, eventdata, handles)
% hObject    handle to inputFunction (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function lowerBound_Callback(hObject, eventdata, handles)
% hObject    handle to lowerBound (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of lowerBound as text
%        str2double(get(hObject,'String')) returns contents of lowerBound as a double


% --- Executes during object creation, after setting all properties.
function lowerBound_CreateFcn(hObject, eventdata, handles)
% hObject    handle to lowerBound (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function upperBound_Callback(hObject, eventdata, handles)
% hObject    handle to upperBound (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of upperBound as text
%        str2double(get(hObject,'String')) returns contents of upperBound as a double


% --- Executes during object creation, after setting all properties.
function upperBound_CreateFcn(hObject, eventdata, handles)
% hObject    handle to upperBound (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function toller_Callback(hObject, eventdata, handles)
% hObject    handle to toller (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of toller as text
%        str2double(get(hObject,'String')) returns contents of toller as a double


% --- Executes during object creation, after setting all properties.
function toller_CreateFcn(hObject, eventdata, handles)
% hObject    handle to toller (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in calcValue.
function calcValue_Callback(hObject, eventdata, handles)
% hObject    handle to calcValue (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
%func=str2num(get(EditRate, 'String'))
%lowBound=str2num(get(EditRate, 'String'))
%upBound=str2num(get(EditRate, 'String'))
%toler=str2num(get(EditRate, 'String'))
syms x;
%tol = 1.e-6;

tol=str2num(get(handles.toller,'String'));
a=str2num(get(handles.lowerBound,'String'));
b=str2num(get(handles.upperBound,'String'));
F = vectorize(inline(get(handles.inputFunction,'string'),'x'));
%F=str2func(get(handles.inputFunction,'String'))
% Initialization
c = (a + b)/2;
%fa = F(a);
%fc = F(c);
%fb = F(b);
fa=subs(F,x,a);
fb=subs(F,x,b);
fc=subs(F,x,c);

% Recursive call
[Q,k] = quadtxstep(F, a, b, tol, fa, fc, fb);
fcount = k + 3;
%bf=str2num(get(handles.inputFunction,'String'));
set(handles.returnData,'String',num2str(Q));


function [Q,fcount] = quadtxstep(F,a,b,tol,fa,fc,fb)

syms x;
% Recursive subfunction used by quadtx.
h = b - a;
c = (a + b)/2;

%fd = F((a+c)/2);
%fe = F((c+b)/2);
sub1=(a+c)/2;
sub2=(c+b)/2;
fd=subs(F,x,sub1);
fe=subs(F,x,sub2);



Q1 = h/6 * (fa + 4*fc + fb);
Q2 = h/12 * (fa + 4*fd + 2*fc + 4*fe + fb);
if abs(Q2 - Q1) <= tol
    Q = Q2 + (Q2 - Q1)/15;
    fcount = 2;
else
    [Qa,ka] = quadtxstep(F, a, c, tol, fa, fd, fc);
    [Qb,kb] = quadtxstep(F, c, b, tol, fc, fe, fb);
    Q = Qa + Qb;
    fcount = ka + kb + 2;
end




% --- Executes on button press in plotHere.
function plotHere_Callback(hObject, eventdata, handles)
% hObject    handle to plotHere (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
a=str2num(get(handles.lowerBound,'String'));
b=str2num(get(handles.upperBound,'String'));
F = vectorize(inline(get(handles.inputFunction,'string'),'x'));
p=ezplot(F,[a,b]);
%set(p,'Parent', plotHere)
%plot(handles.axes1,F,a,b)






function returnData_Callback(hObject, eventdata, handles)
% hObject    handle to returnData (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of returnData as text
%        str2double(get(hObject,'String')) returns contents of returnData as a double


% --- Executes during object creation, after setting all properties.
function returnData_CreateFcn(hObject, eventdata, handles)
% hObject    handle to returnData (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
