#include<windows.h>
#include "Window.h"

#define WIDTH 800
#define HEIGHT 600



// Global  callback Function Declaration
LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);

// Dialog  Declaration
BOOL CALLBACK MyDlgProc(HWND,UINT,WPARAM, LPARAM);

//Global declaration 
HWND hwnd;
unsigned int drawTextFlag = 0;



//Entry-Point Funtion
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpszCmdLine, int iCmdShow)
{
	//variable declarations
	WNDCLASSEX wndclass;
	TCHAR szAppName[] = TEXT("RRJ_Window");
	
	MSG msg;

	//code
	memset((void*)&wndclass, 0, sizeof(WNDCLASSEX));

	//Initializing window class
	wndclass.cbSize        = sizeof(WNDCLASSEX);
	wndclass.style         = CS_HREDRAW | CS_VREDRAW;
	wndclass.cbClsExtra    = 0;
	wndclass.cbWndExtra = 0;
	wndclass.hInstance     = hInstance;
	wndclass.hbrBackground = (HBRUSH)GetStockObject(BLACK_BRUSH);
	wndclass.hIcon = LoadIcon(hInstance, MAKEINTRESOURCE(RRJ_ICON));
	wndclass.hIconSm = LoadIcon(hInstance, MAKEINTRESOURCE(RRJ_ICON));
	wndclass.hCursor = LoadCursor(NULL, IDC_ARROW);
	wndclass.lpfnWndProc = WndProc;
	wndclass.lpszClassName = szAppName;
	wndclass.lpszMenuName = NULL;

	//Register the above Window Class
	RegisterClassEx(&wndclass);

	// Create the Window
	hwnd = CreateWindow(szAppName,
		TEXT("RRJ: My First Window"),
		WS_OVERLAPPEDWINDOW,
		0,
		0,
		WIDTH,
		HEIGHT,
		NULL,
		NULL,
		hInstance,
		NULL);

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
	static HINSTANCE hInstance;
	RECT rect;
	PAINTSTRUCT ps;
	HDC hdc = NULL;
	TCHAR str[255];
	

	
	//code
	switch (iMsg)
	{
	case WM_CREATE:
		hInstance = (HINSTANCE ) GetWindowLongPtr(hwnd, GWLP_HINSTANCE);
		break;

	case WM_PAINT:
        memset((void*)&rect, 0, sizeof(RECT));
		GetClientRect(hwnd, &rect);
		memset((void*)&ps, 0, sizeof(PAINTSTRUCT));
		hdc = BeginPaint(hwnd, &ps);
		if (drawTextFlag == 1)
		{
			wsprintf(str, TEXT("OK BUTTON CLICKED!"));
			SetBkColor(hdc, TRANSPARENT);
			
			SetTextColor(hdc, RGB(0, 255, 0));
			DrawText(hdc, str, -1, &rect, DT_SINGLELINE | DT_CENTER | DT_VCENTER);

			if(hdc)
			{
				EndPaint(hwnd,&ps);
				hdc = NULL;

			}

		}
		else if (drawTextFlag == 2)
		{
			wsprintf(str, TEXT("CANCEL BUTTON CLICKED!"));
			SetBkColor(hdc, TRANSPARENT);
			SetTextColor(hdc, RGB(0, 255, 0));
			DrawText(hdc, str, -1, &rect, DT_SINGLELINE | DT_CENTER | DT_VCENTER);

			if(hdc)
			{
				EndPaint(hwnd,&ps);
				hdc = NULL;

			}

		}
		//check
		else
		{
			wsprintf(str, TEXT("PRESS SPACEBAR TO OPEN DIALOG BOX"));
			SetBkColor(hdc, TRANSPARENT);
			SetTextColor(hdc, RGB(255, 255, 255));
			DrawText(hdc, str, -1, &rect, DT_SINGLELINE | DT_CENTER | DT_VCENTER);

			if(hdc)
			{
				EndPaint(hwnd,&ps);
				hdc = NULL;

			}

		}

	case WM_KEYDOWN:
		switch (wParam)
		{
		case VK_ESCAPE:
			DestroyWindow(hwnd);
			break;
			
		case VK_SPACE:
		    DialogBox(hInstance, MAKEINTRESOURCE(DIALOGBOX), hwnd, (DLGPROC)MyDlgProc);
			break;
		}
		break;

	

	case WM_DESTROY:
		
		PostQuitMessage(0);
		break;

	default:
		break;
	}
	return (DefWindowProc(hwnd, iMsg, wParam, lParam));	

	
}

BOOL CALLBACK MyDlgProc(HWND hwndDlg, UINT iMsg, WPARAM wParam, LPARAM lParam)
{
	switch(iMsg)
	{
		case WM_INITDIALOG:
			return (TRUE);
		
		case WM_COMMAND:
		     switch(LOWORD(wParam))
			 {
				case ID_OK:
					drawTextFlag = 1; 
					InvalidateRect(hwnd, NULL, TRUE);
					EndDialog(hwndDlg,0);
				break;

				case ID_CANCEL:
				    drawTextFlag = 2;
				    InvalidateRect(hwnd, NULL, TRUE);
				    EndDialog(hwndDlg,0);
				break;


			 }
			break;
	}
	return (FALSE);
	
}
