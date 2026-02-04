#include<windows.h>
#include "Window.h"

// Global  callback Function Declaration
LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);

//Entry-Point Funtion
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpszCmdLine, int iCmdShow)
{
	//variable declarations
	WNDCLASSEX wndclass;
	TCHAR szAppName[] = TEXT("RRJ_Window");
	HWND hwnd;
	MSG msg;

	//code
	memset((void*)&wndclass, 0, sizeof(WNDCLASSEX));

	//Initializing window class
	wndclass.cbSize        = sizeof(WNDCLASSEX);
	wndclass.style         = CS_HREDRAW | CS_VREDRAW;
	wndclass.cbClsExtra    = 0;
	wndclass.cbWndExtra     = 0;
	wndclass.hInstance     = hInstance;
	wndclass.hbrBackground = (HBRUSH)GetStockObject(BLACK_BRUSH);
	wndclass.hIcon = LoadIcon(hInstance, MAKEINTRESOURCE(RRJ_ICON));
	wndclass.hIconSm       = LoadIcon(hInstance, IDI_APPLICATION);
	wndclass.hCursor = LoadCursor(NULL, IDC_ARROW);
	wndclass.lpfnWndProc = WndProc;
	wndclass.lpszClassName = szAppName;
	wndclass.lpszMenuName = NULL;

	//Register the above Window Class
	RegisterClassEx(&wndclass);

	// Create the Window
	hwnd = CreateWindow(
    szAppName,
    TEXT("RRJ: My First Window"),
    WS_OVERLAPPEDWINDOW,
    CW_USEDEFAULT,
    CW_USEDEFAULT,
    400,        // width
    400,        // height
    NULL,       
    NULL,       
    hInstance,
    NULL
);


	//Show the window
	ShowWindow(hwnd, iCmdShow);

	// Update the window
	UpdateWindow(hwnd);

	//Message Loop
	while (GetMessage(&msg, NULL, 0, 0)) // 
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);

	}

	return((int)msg.wParam);


}

//Window Procedure
LRESULT CALLBACK WndProc(HWND hwnd, UINT iMsg, WPARAM wParam, LPARAM lParam)
{
	//variable declrations
	PAINTSTRUCT ps;
	HDC hdc,hMemDC;
	static HBITMAP hBitmap;
	static unsigned int resizedWindowHeight =0;
	static unsigned int resizedWindowWidth = 0;
	
	//code
	switch (iMsg)
	{
	case WM_CREATE:
	    hBitmap = LoadBitmap(((LPCREATESTRUCT)lParam)->hInstance, MAKEINTRESOURCE(RRJ_MYBITMAP));
		InvalidateRect(hwnd, NULL, TRUE);
 // to call WM_PAINT
		break;

	case WM_PAINT:
		hdc = BeginPaint(hwnd, &ps);
		hMemDC = CreateCompatibleDC(hdc);
		SelectObject(hMemDC, hBitmap);
		SetStretchBltMode(hdc, COLORONCOLOR);
		StretchBlt(hdc, 0, 0, resizedWindowWidth, resizedWindowHeight, hMemDC, 0, 0,1079,1079, SRCCOPY);

        if(hMemDC)
		{
			DeleteDC(hMemDC);
			hMemDC = NULL;
		}
		if(hdc)
		{
			EndPaint(hwnd, &ps);
			hdc = NULL;
		}
		
		break;

	case WM_KEYDOWN:
		switch(LOWORD (wParam))
		{
		case VK_ESCAPE:
			DestroyWindow(hwnd);
			break;
		default:
			break;
		}
		break;


	case WM_SIZE:
	resizedWindowWidth = LOWORD(lParam);
		resizedWindowHeight = HIWORD(lParam);
		
		break;
	

	case WM_DESTROY:
		DeleteObject(hBitmap);
		PostQuitMessage(0);
		break;

	default:
		break;
	}

	return (DefWindowProc(hwnd, iMsg, wParam, lParam));
}


