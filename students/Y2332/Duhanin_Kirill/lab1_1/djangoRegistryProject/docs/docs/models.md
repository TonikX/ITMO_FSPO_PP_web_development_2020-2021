### Models
#### Building
> ������ ������������

- **list** building/list -- ������ ���� ��������
- **detail** building/<int:pk> -- ����������� �� ������� � id = pk
- **create** building/create -- ������� ������
- **delete** building/<int:pk>/delete -- ������� ������ � id = pk
- **update** building/<int:pk>/update -- ���������� ������ ������� � id = pk
#### Department
> ������������� ������������ (�������, �������, �������������� �����)

- **list** department/list -- ������ ���� ��������
- **detail** department/<int:pk> -- ����������� �� ������� � id = pk
- **create** department/create -- ������� ������
- **delete** department/<int:pk>/delete -- ������� ������ � id = pk
- **update** department/<int:pk>/update -- ���������� ������ ������� � id = pk
#### Worker
> �������� ������������. ����� ���������� �������������� ��� ����� ��������������� �� ��������� 

- **list** worker/list -- ������ ���� ��������
- **detail** worker/<int:pk> -- ����������� �� ������� � id = pk
- **create** worker/create -- ������� ������
- **delete** worker/<int:pk>/delete -- ������� ������ � id = pk
- **update** worker/<int:pk>/update -- ���������� ������ ������� � id = pk
#### Management
> ���������� ��������� ����������� ����� ���������� � ��������������

- **list** management/list -- ������ ���� ��������
- **detail** management/<int:pk> -- ����������� �� ������� � id = pk
- **create** management/create -- ������� ������
- **delete** management/<int:pk>/delete -- ������� ������ � id = pk
- **update** management/<int:pk>/update -- ���������� ������ ������� � id = pk
#### Hall
> ��������� ���������� �� ��������������. ����� ���� ������������ �������, ������� ����� ��� ���������� ���������

- **list** hall/list -- ������ ���� ��������
- **detail** hall/<int:pk> -- ����������� �� ������� � id = pk
- **create** hall/create -- ������� ������
- **delete** hall/<int:pk>/delete -- ������� ������ � id = pk
- **update** hall/<int:pk>/update -- ���������� ������ ������� � id = pk
#### Responsibility
> ��������������� ��������� �� ����������

- **list** responsibility/list -- ������ ���� ��������
- **detail** responsibility/<int:pk> -- ����������� �� ������� � id = pk
- **create** responsibility/create -- ������� ������
- **delete** responsibility/<int:pk>/delete -- ������� ������ � id = pk
- **update** responsibility/<int:pk>/update -- ���������� ������ ������� � id = pk
#### Property
> �������, ���������� ������ ����������� �����

- **list** property/list -- ������ ���� ��������
- **detail** property/<int:pk> -- ����������� �� ������� � id = pk
- **create** property/create -- ������� ������
- **delete** property/<int:pk>/delete -- ������� ������ � id = pk
- **update** property/<int:pk>/update -- ���������� ������ ������� � id = pk
#### Unit
> ������� ��������� ���������� �� ���������� ����������� �������� Consist

- **list** unit/list -- ������ ���� ��������
- **detail** unit/<int:pk> -- ����������� �� ������� � id = pk
- **create** unit/create -- ������� ������
- **delete** unit/<int:pk>/delete -- ������� ������ � id = pk
- **update** unit/<int:pk>/update -- ���������� ������ ������� � id = pk
#### Consist
> ���������� ��������� ��������� � ������� ��������� 

- **list** consist/list -- ������ ���� ��������
- **detail** consist/<int:pk> -- ����������� �� ������� � id = pk
- **create** consist/create -- ������� ������
- **delete** consist/<int:pk>/delete -- ������� ������ � id = pk
- **update** consist/<int:pk>/update -- ���������� ������ ������� � id = pk
#### Revaluation
> ���������� 

- **list** revaluation/list -- ������ ���� ��������
- **detail** revaluation/<int:pk> -- ����������� �� ������� � id = pk
- **create** revaluation/create -- ������� ������
- **delete** revaluation/<int:pk>/delete -- ������� ������ � id = pk
- **update** revaluation/<int:pk>/update -- ���������� ������ ������� � id = pk