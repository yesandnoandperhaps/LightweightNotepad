import matplotlib.pyplot as plt
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import torch_directml
from sklearn.linear_model import LinearRegression as SLinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler, RobustScaler
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

class FeatureScaling:
    def __init__(self, feature_scaling, csv_path, input_columns="0,0",output_columns="1,1", device='gpu',start=True) -> None:
        self.start = start
        self.user_device = device.lower()
        self.input_columns = self.extract_columns(input_columns)
        self.output_columns = self.extract_columns(output_columns)
        self.feature_scaling_method = feature_scaling
        self.data = self.load_data(csv_path, self.input_columns)#特征数据
        self.output_data = self.load_data(csv_path, self.output_columns)#目标数据
        self.actual_device = self.__get_device()

    @staticmethod
    def extract_columns(columns_str):
        columns_str = columns_str.replace('，', ',')
        return [int(col.strip()) for col in columns_str.split(',')]

    @staticmethod
    def load_data(csv_path, columns_to_read):
        start_col, end_col = columns_to_read
        data = pd.read_csv(csv_path, encoding='utf-8', usecols=range(start_col, end_col + 1))
        return data

    @staticmethod
    def __get_device():
        if torch.cuda.is_available():
            return torch.device('cuda')
        elif torch_directml.is_available():
            return torch_directml.device()
        else:
            return torch.device('cpu')

    def __to_tensor(self, data):
        return torch.tensor(data.values, dtype=torch.float32, device=self.actual_device)

    def feature_scaling(self):
        methods_cpu = {
            "min-max_normalization": self.__min_max_normalization_cpu,
            "mean_normalization": self.__mean_normalization_cpu,
            "z-score_normalization": self.__z_score_normalization_cpu,
            "max_abs_normalization": self.__max_abs_normalization_cpu,
            "robust_standardization": self.__robust_standardization_cpu
        }

        methods_gpu = {
            "min-max_normalization": self.__min_max_normalization_gpu,
            "mean_normalization": self.__mean_normalization_gpu,
            "z-score_normalization": self.__z_score_normalization_gpu,
            "max_abs_normalization": self.__max_abs_normalization_gpu,
            "robust_standardization": self.__robust_standardization_gpu
        }
        if self.start:
            if self.user_device == "cpu":
                return methods_cpu[self.feature_scaling_method](),self.output_data,len(self.data.columns.tolist()),len(self.output_data.columns.tolist()),torch.device('cpu')
            else:
                if self.actual_device == torch.device('cpu'):
                    if self.user_device == "强制cpu操作pytorch":
                        return methods_gpu[self.feature_scaling_method](), self.output_data, len(self.data.columns.tolist()), len(self.output_data.columns.tolist()), self.user_device
                    return methods_cpu[self.feature_scaling_method](),self.output_data,len(self.data.columns.tolist()),len(self.output_data.columns.tolist()),self.actual_device
                else:
                    return methods_gpu[self.feature_scaling_method](),self.output_data,len(self.data.columns.tolist()),len(self.output_data.columns.tolist()),self.actual_device
        else:
            return self.data, self.output_data, len(self.data.columns.tolist()), len(self.output_data.columns.tolist()), torch.device('cpu')
    def __min_max_normalization_cpu(self):
        scaler_object = MinMaxScaler()
        return pd.DataFrame(scaler_object.fit_transform(self.data), columns=self.data.columns)

    def __mean_normalization_cpu(self):
        scaler_object = MinMaxScaler()
        scaler_object_data = pd.DataFrame(scaler_object.fit_transform(self.data), columns=self.data.columns)
        return scaler_object_data - scaler_object_data.mean()

    def __z_score_normalization_cpu(self):
        scaler_object = StandardScaler()
        return pd.DataFrame(scaler_object.fit_transform(self.data), columns=self.data.columns)

    def __max_abs_normalization_cpu(self):
        scaler_object = MaxAbsScaler()
        return pd.DataFrame(scaler_object.fit_transform(self.data), columns=self.data.columns)

    def __robust_standardization_cpu(self):
        scaler_object = RobustScaler()
        return pd.DataFrame(scaler_object.fit_transform(self.data), columns=self.data.columns)

    def __min_max_normalization_gpu(self):
        data_tensor = self.__to_tensor(self.data)
        min_vals = data_tensor.min(dim=0, keepdim=True)[0]
        max_vals = data_tensor.max(dim=0, keepdim=True)[0]
        scaled_tensor = (data_tensor - min_vals) / (max_vals - min_vals)
        return pd.DataFrame(scaled_tensor.cpu().numpy(), columns=self.data.columns)

    def __mean_normalization_gpu(self):
        data_tensor = self.__to_tensor(self.data)
        min_vals = data_tensor.min(dim=0, keepdim=True)[0]
        max_vals = data_tensor.max(dim=0, keepdim=True)[0]
        mean_vals = data_tensor.mean(dim=0, keepdim=True)
        scaled_tensor = (data_tensor - mean_vals) / (max_vals - min_vals)
        return pd.DataFrame(scaled_tensor.cpu().numpy(), columns=self.data.columns)

    def __z_score_normalization_gpu(self):
        data_tensor = self.__to_tensor(self.data)
        mean_vals = data_tensor.mean(dim=0, keepdim=True)
        std_vals = data_tensor.std(dim=0, keepdim=True)
        scaled_tensor = (data_tensor - mean_vals) / std_vals
        return pd.DataFrame(scaled_tensor.cpu().numpy(), columns=self.data.columns)

    def __max_abs_normalization_gpu(self):
        data_tensor = self.__to_tensor(self.data)
        max_vals = data_tensor.abs().max(dim=0, keepdim=True)[0]
        scaled_tensor = data_tensor / max_vals
        return pd.DataFrame(scaled_tensor.cpu().numpy(), columns=self.data.columns)

    def __robust_standardization_gpu(self):
        data_tensor = self.__to_tensor(self.data)
        median_vals = data_tensor.median(dim=0, keepdim=True)[0]
        q1_vals = torch.quantile(data_tensor, 0.25, dim=0, keepdim=True)
        q3_vals = torch.quantile(data_tensor, 0.75, dim=0, keepdim=True)
        scaled_tensor = (data_tensor - median_vals) / (q3_vals - q1_vals)
        return pd.DataFrame(scaled_tensor.cpu().numpy(), columns=self.data.columns)


class LinearRegression:
    def __init__(self, lr_optimization, lr_loss_function, lr_a_scheduler,
                 lr_a,lr_e,
                 feature_scaling,
                 csv_path, input_columns="0,0",output_columns="1,1",
                 device='cpu',
                 lr_m = 0,lr_d=0,lr_w=0,lr_n=False
                 ):
        """
        #用户输入
        :param lr_optimization:梯度下降方法【未来实现更多】
        :param lr_loss_function:损失函数
        :param lr_a_scheduler:学习率优化器
        :param lr_a:学习率
        :param lr_e:训练次数
        :param lr_m:动量
        :param lr_d:动量衰减
        :param lr_w:权重衰减
        :param lr_n:Nesterov动量
        :param csv_path:数据文件
        :param input_columns:特征数据指针
        :param output_columns:目标数据指针
        :param device:硬件 cpu or gpu

        #代码操作
        :param feature_scaling:调用特征缩放

        """

        self.a_scheduler = lr_a_scheduler
        self.a = lr_a
        self.e = lr_e
        self.d = lr_d
        self.m = lr_m
        self.n = lr_n
        self.w = lr_w
        self.feature_scaling,self.output,input_size,output_size,self.actual_device = FeatureScaling(feature_scaling,csv_path,input_columns,output_columns,device,True).feature_scaling()
        print(self.feature_scaling)
        self.features,self.target = self.pytorch_tensor()
        self.model = self.LinearRegressionModule(input_size, output_size).to(self.actual_device)
        self.actual_loss_function = self.criterion_loss_function(lr_loss_function)
        self.actual_optimization = self.optimization_methods(lr_optimization,self.model,self.a,self.m,self.d,self.w,self.n)
        self.losses = []

    class LinearRegressionModule(nn.Module):
        def __init__(self,input_size,output_size):
            super(LinearRegression.LinearRegressionModule, self).__init__()
            self.linear = nn.Linear(input_size, output_size)

        def forward(self, x):
            return self.linear(x)

    def linear_regression(self):
        print(self.actual_device)
        if self.actual_device == torch.device('cpu'):
            feature_scaling = self.feature_scaling.to_numpy()
            output = self.output.to_numpy()
            reg = SLinearRegression()
            reg.fit(feature_scaling, output)
            print("Coefficients:", reg.coef_)
            print("Intercepts:", reg.intercept_)
            score = reg.score(feature_scaling, output)
            print("Score:", score)

            return reg
        elif self.actual_device == "强制cpu操作pytorch":
            self.actual_device = torch.device('cpu')
            self.pytorch_linear_regression_bgd()
        else:
            self.pytorch_linear_regression_bgd()

    @staticmethod
    def criterion_loss_function(user_loss_function):
        loss_functions = {
            "mean_squared_error": nn.MSELoss,
            "均方误差": nn.MSELoss,
            "mean_absolute_error": nn.L1Loss,
            "绝对误差": nn.L1Loss,
            "huber_loss": nn.SmoothL1Loss,
            "Huber损失": nn.SmoothL1Loss
        }
        return loss_functions.get(user_loss_function, nn.MSELoss)()

    @staticmethod
    def optimization_methods(lr_optimization,model,a,m,d,w,n):
        optimization_dictionary = {
            "batch_GD": lambda: optim.SGD(model.parameters(), lr=a, momentum=m, dampening=d, weight_decay=w,
                                          nesterov=n),
            "批量梯度下降": lambda: optim.SGD(model.parameters(), lr=a, momentum=m, dampening=d, weight_decay=w,
                                              nesterov=n),
            "stochastic_GD": lambda: optim.SGD(model.parameters(), lr=a, momentum=m, dampening=d, weight_decay=w,
                                               nesterov=n),
            "随机梯度下降": lambda: optim.SGD(model.parameters(), lr=a, momentum=m, dampening=d, weight_decay=w,
                                              nesterov=n),
            "mini-batch_GD": lambda: optim.SGD(model.parameters(), lr=a, momentum=m, dampening=d, weight_decay=w,
                                               nesterov=n),
            "小批量梯度下降": lambda: optim.SGD(model.parameters(), lr=a, momentum=m, dampening=d, weight_decay=w,
                                                nesterov=n)
        }
        return optimization_dictionary[lr_optimization]()

    def pytorch_tensor(self):
        x = torch.tensor(self.feature_scaling.to_numpy(), device=self.actual_device, dtype=torch.float32)
        y = torch.tensor(self.output.to_numpy(), device=self.actual_device, dtype=torch.float32)
        return x, y

    def pytorch_linear_regression_bgd(self):

        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            self.actual_optimization, mode='min', factor=0.5, patience=10, min_lr=1e-30
        )

        for _ in range(self.e):
            self.model.train()

            outputs = self.model(self.features)
            loss = self.actual_loss_function(outputs,self.target)

            self.losses.append(loss.item())
            loss.backward()
            # 获取模型的参数和梯度
            device_params = [param for param in self.model.parameters() if param.requires_grad]
            device_grads = [param.grad for param in self.model.parameters() if param.requires_grad]

            # 使用 torch.no_grad() 避免在计算图中产生梯度
            with torch.no_grad():
                lr = self.actual_optimization.param_groups[0]['lr']  # 从优化器中获取学习率
                for i in range(len(device_params)):
                    device_params[i].sub_(device_grads[i] * lr)

            self.actual_optimization.zero_grad()

            scheduler.step(loss)

            current_lr = scheduler.optimizer.param_groups[0]['lr']
            if (_ + 1) % 1000 == 0:
                print(f'Epoch [{_ + 1}/{self.e}], Loss: {loss.item():.4f}, Learning Rate: {current_lr:.6f}')
        # 打印模型参数
        print("训练后的模型参数:")
        for name, param in self.model.named_parameters():
            print(f"{name}: {param.data}")

        # 在训练结束后进行评估
        self.model.eval()
        with torch.no_grad():
            predictions = self.model(self.features)
            true_values = self.target.cpu().numpy()
            predicted_values = predictions.cpu().numpy()

            # 计算评估指标
            mse = mean_squared_error(true_values, predicted_values)
            rmse = mse ** 0.5
            r2 = r2_score(true_values, predicted_values)

            print(f'均方误差 (MSE): {mse:.4f}')
            print(f'均方根误差 (RMSE): {rmse:.4f}')
            print(f'R^2 分数: {r2:.4f}')
            print(f'模型结果：{self.model.state_dict()}')

            # 计算残差
            residuals = true_values - predicted_values

            # 绘制损失图
            plt.figure(figsize=(7, 5))
            plt.plot(range(1, self.e + 1), self.losses, color='b')
            plt.xlabel('迭代次数 (Epoch)')
            plt.ylabel('损失值')
            plt.title('训练过程中损失值变化')
            plt.show()

            # 绘制残差图
            plt.figure(figsize=(7, 5))
            plt.scatter(predicted_values, residuals, alpha=0.5)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.xlabel('预测值')
            plt.ylabel('残差')
            plt.title('残差与预测值的关系')
            plt.show()

            # 绘制残差直方图
            plt.figure(figsize=(7, 5))
            plt.hist(residuals, bins=30, edgecolor='k', alpha=0.7)
            plt.xlabel('残差')
            plt.ylabel('频率')
            plt.title('残差直方图')
            plt.show()

            # 绘制合并图
            plt.figure(figsize=(14, 7))

            # 绘制损失图
            plt.subplot(1, 3, 1)
            plt.plot(range(1, self.e + 1), self.losses, color='b')
            plt.xlabel('迭代次数 (Epoch)')
            plt.ylabel('损失值')
            plt.title('训练过程中损失值变化')

            # 绘制残差图
            plt.subplot(1, 3, 2)
            plt.scatter(predicted_values, residuals, alpha=0.5)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.xlabel('预测值')
            plt.ylabel('残差')
            plt.title('残差与预测值的关系')

            # 绘制残差直方图
            plt.subplot(1, 3, 3)
            plt.hist(residuals, bins=30, edgecolor='k', alpha=0.7)
            plt.xlabel('残差')
            plt.ylabel('频率')
            plt.title('残差直方图')

            plt.tight_layout()
            plt.show()

    '''
    def pytorch_linear_regression_sgd(self):
        for _ in range(self.e):
            self.model.train()

            outputs = self.model(self.features)
            loss = self.actual_loss_function(outputs, self.target)

            loss.backward()
            self.actual_optimization.step()
            self.actual_optimization.zero_grad()
    '''

    @staticmethod
    def whether_scheduler(optimization):
        pass
        '''
        scheduler_dict = {
            "None":lambda:None
            "LambdaLR":lambda:LambdaLR(optimization, lr_lambda = , last_epoch=- 1, verbose=False)
            "StepLR":()
            "MultiStepLR":()
            "ExponentialLR":()
            "CosineAnnealingLR":()
            "ReduceLROnPlateau":()
            "CyclicLR",
            "OneCycleLR",
            "CosineAnnealingWarmRestarts",
            "PolynomialLR",
            "ConstantLR",
            "ChainedScheduler"
        }
        '''
if __name__ == '__main__':
    path = r"D:\LightweightNotepad\工作簿2.csv"
    scaler = LinearRegression("批量梯度下降", "均方误差","a",0.1,10000,"min-max_normalization",path,"0,4","5,6","gpu")
    scaled_data = scaler.linear_regression()
    print(scaled_data)