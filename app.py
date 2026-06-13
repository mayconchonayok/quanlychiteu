import logging
from report import ReportCache, hien_thi_tong_quan, hien_thi_bao_cao_thang, hien_thi_chi_theo_danh_muc, hien_thi_bao_cao_nam
from transaction import them_giao_dich, sua_giao_dich, xoa_giao_dich, tim_giao_dich_theo_ma, tim_giao_dich_theo_ngay, tim_giao_dich_theo_loai
from category import them_danh_muc, sua_danh_muc, xoa_danh_muc, hien_thi_danh_muc
from budget import them_ngan_sach, hien_thi_ngan_sach
from export_report import xuat_bao_cao_txt, xuat_bao_cao_csv, ve_bieu_do_cot, ve_bieu_do_tron
from fileio import load_transactions, save_transactions, load_budgets, save_budgets, load_categories, save_categories
from validators import read_month

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)


class ExpenseApp:
    def __init__(self):
        self.transactions = None
        self.categories = None
        self.budgets = None
        self.cache = ReportCache()

    async def load_data(self):
        self.transactions = await load_transactions()
        self.categories = await load_categories()
        self.budgets = await load_budgets()
        logging.info('Đã nạp dữ liệu')

    async def save_all(self):
        await save_transactions(self.transactions)
        await save_categories(self.categories)
        await save_budgets(self.budgets)
        logging.info('Đã lưu dữ liệu')

    def show_menu(self):
        print('\n========== QUẢN LÝ CHI TIÊU CÁ NHÂN ==========', flush=True)
        print('1. Xem danh sách giao dịch')
        print('2. Thêm giao dịch')
        print('3. Sửa giao dịch')
        print('4. Xóa giao dịch')
        print('5. Tìm giao dịch theo mã')
        print('6. Tìm giao dịch theo ngày')
        print('7. Tìm giao dịch theo loại')
        print('8. Xem danh mục')
        print('9. Thêm danh mục')
        print('10. Sửa danh mục')
        print('11. Xóa danh mục')
        print('12. Đặt ngân sách theo tháng')
        print('13. Kiểm tra ngân sách')
        print('14. Báo cáo tổng quan')
        print('15. Báo cáo theo tháng')
        print('16. Chi tiêu theo danh mục + ASCII chart')
        print('17. Xuất báo cáo TXT')
        print('18. Xuất báo cáo CSV')
        print('19. Vẽ biểu đồ cột')
        print('20. Vẽ biểu đồ tròn')
        print('21. Báo cáo theo năm')
        print('0. Lưu và thoát')

    async def run(self):
        await self.load_data()
        while True:
            self.show_menu()
            choice = input('Chọn chức năng: ').strip()
            if choice == '1':
                self.show_transactions()
            elif choice == '2':
                await them_giao_dich(self.transactions, self.categories, save_transactions, self.cache)
                logging.info('Thêm giao dịch')
            elif choice == '3':
                if sua_giao_dich(self.transactions, self.categories, self.cache):
                    await save_transactions(self.transactions)
                    logging.info('Sửa giao dịch')
            elif choice == '4':
                await xoa_giao_dich(self.transactions, save_transactions, self.cache)
                logging.info('Xóa giao dịch')
            elif choice == '5':
                tim_giao_dich_theo_ma(self.transactions)
            elif choice == '6':
                tim_giao_dich_theo_ngay(self.transactions)
            elif choice == '7':
                tim_giao_dich_theo_loai(self.transactions)
            elif choice == '8':
                hien_thi_danh_muc(self.categories)
            elif choice == '9':
                them_danh_muc(self.categories)
                await save_categories(self.categories)
            elif choice == '10':
                sua_danh_muc(self.categories)
                await save_categories(self.categories)
            elif choice == '11':
                xoa_danh_muc(self.categories)
                await save_categories(self.categories)
            elif choice == '12':
                them_ngan_sach(self.budgets, self.categories)
                await save_budgets(self.budgets)
            elif choice == '13':
                hien_thi_ngan_sach(self.transactions, self.budgets)
            elif choice == '14':
                hien_thi_tong_quan(self.transactions)
            elif choice == '15':
                month = read_month('Nhập tháng cần xem (YYYY-MM): ')
                hien_thi_bao_cao_thang(self.transactions, month, self.cache)
            elif choice == '16':
                hien_thi_chi_theo_danh_muc(self.transactions, self.cache)
            elif choice == '17':
                xuat_bao_cao_txt(self.transactions)
            elif choice == '18':
                xuat_bao_cao_csv(self.transactions)
            elif choice == '19':
                ve_bieu_do_cot(self.transactions)
            elif choice == '20':
                ve_bieu_do_tron(self.transactions)
            elif choice == '21':
                year = input('Nhap nam can xem (YYYY): ').strip()
                hien_thi_bao_cao_nam(self.transactions, year)
            elif choice == '0':
                await self.save_all()
                print('Đã lưu dữ liệu. Hẹn gặp lại!')
                break
            else:
                print('Lựa chọn không hợp lệ. Vui lòng nhập lại.')

    def show_transactions(self):
        if len(self.transactions) == 0:
            print('Chưa có giao dịch nào.')
            return
        print('\n ID | Ngày       | Loại | Danh mục        |      Số tiền | Ghi chú')
        print('-' * 78)
        for t in self.transactions:
            print(t)
