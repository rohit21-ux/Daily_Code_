#include<windows.h>

//Global callback function declaration
LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);

//Entry -point function
int WINAPI WinMain(HINSTANCE hInstance , HINSTANCE hPrevInstance,LPSTR lpszCmdLine , int iCmdShow)
{

	//variable declaration
	WNDCLASSEX wndclass;
	TCHAR szAppName[] = TEXT("RRJ_Window");
	HWND hwnd;
	MSG msg;

	// code
	memset((void*)&wndclass, 0, sizeof(WNDCLASSEX));

	//Initializing window class
	wndclass.cbSize   = sizeof(WNDCLASSEX);
	wndclass.style    = CS_HREDRAW | CS_VREDRAW;
	wndclass.cbClsExtra  =  0;
	wndclass.cbWndExtra  =0;
	wndclass.hInstance  = hInstance;
	wndclass.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
	wndclass.hIcon = LoadIcon(NULL,IDI_APPLICATION);
	wndclass.hIconSm   = LoadIcon(NULL, IDC_ARROW);
	wndclass.lpfnWndProc  = WndProc;
	wndclass.lpszClassName  = szAppName;
	wndclass.lpszMenuName  = NULL;

	//Register the above window class 
	RegisterClassEx(&wndclass);


	// create the window
	hwnd = CreateWindow(szAppName,
		TEXT("RRJ: My First Window"),
		WS_OVERLAPPEDWINDOW,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		NULL,
		NULL,
		hInstance,
		NULL);

	//Show the window
	ShowWindow(hwnd,iCmdShow);

	//update the window
	UpdateWindow(hwnd);

	//Message loop 
	while (GetMessage(&msg,NULL,0,0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);

	}

	return((int)msg.wParam);

}

//Window procedure
LRESULT CALLBACK WndProc(HWND hwnd , UINT iMsg, WPARAM wParam, LPARAM lParam)
{

	//variable declaration
	switch(iMsg)
	{
	case WM_DESTROY:
		PostQuitMessage(0);
		break;
	default:
		break;

	}
	return (DefWindowProc(hwnd , iMsg ,  wParam , lParam));
}



