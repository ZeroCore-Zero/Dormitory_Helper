<template>
    <div id="myapp">
        <div class="chart-container">
            <canvas id="myChart"></canvas>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { Chart, registerables } from 'chart.js';
import zoomPlugin from 'chartjs-plugin-zoom';
import 'chartjs-adapter-luxon';

Chart.register(...registerables, zoomPlugin);

export default {
    name: 'App',
    data() {
        return {
            chart: null,
            remainingData: [],
            speedData: [],
            intervalId: null  // 存储 setInterval 的 ID
        };
    },
    async mounted() {
        await this.update();
        this.intervalId = setInterval(async () => {await this.update();}, 60000);  // 每分钟更新数据
    },
    beforeUnmount() {
        // 清理定时器，防止组件销毁时继续触发
        if (this.intervalId) {
            clearInterval(this.intervalId);
        }
        if (this.chart) {
            this.chart.destroy();
        }
    },
    methods: {
        async update() {
            this.remainingData = await this.fetchData();
            this.calculateSpeed();
            if (this.chart) {
                this.chart.destroy();
            }
            this.createChart();
        },
        async fetchData() {
            return await axios.get('http://localhost:5000/data')
            .then(response => {
                console.log('Received Data:', response.data);
                return response.data.map(item => {
                    return { x: new Date(item.timestamp), y: item.remaining };
                });
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
        },
        calculateSpeed() {
            const speeds = [];
            let lastFee = this.remainingData[0].y;
            for (let i = 1; i < this.remainingData.length; i++) {
                const speed = lastFee - this.remainingData[i].y;
                if (speed === 0) {
                    continue;
                }
                lastFee = this.remainingData[i - 1].y;
                speeds.push({ x: this.remainingData[i].x, y: speed });
            }
            this.speedData = speeds;
        },
        createChart() {
            const canvasElement = document.getElementById('myChart');
            const dataset = [
                {
                    label: 'Remaining',
                    yAxisID: 'remaining-y-axis',
                    data: this.remainingData,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                },
                {
                    label: 'Speed',
                    data: this.speedData,
                    yAxisID: 'speed-y-axis',
                    borderColor: 'rgb(255, 99, 132)',
                    tension: 0.1
                }
            ];
            let option = {};
            option.scales = {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute',
                        tooltipFormat: 'yyyy-MM-dd HH:mm',
                        displayFormats: {
                            minute: 'yyyy-MM-dd HH:mm'
                        }
                    },
                    // max: new Date(),
                    // min: oneHourAgo,
                },
                "remaining-y-axis": {
                    id: 'remaining-y-axis',
                    type: 'linear',
                    position: 'left'
                },
                "speed-y-axis": {
                    id: 'speed-y-axis',
                    type: 'linear',
                    position: 'right'
                }
            };
            option.plugins = {
                title: {
                    display: true,
                    text: 'Electron Monitor'
                },
                subtitle: {
                    display: true,
                    text: 'Surplus: ' + this.remainingData[0].y
                },
                tooltip: {
                    mode: 'index',
                    position: 'nearest'
                },
                legend: {
                    onClick: (e, legendItem, legend) => {
                        const datasetIndex = legendItem.datasetIndex;
                        const dataset = legend.chart.data.datasets[datasetIndex];

                        // 确保点击图例时，数据集存在并且被初始化
                        if (!dataset || !dataset.data || !Array.isArray(dataset.data)) {
                            console.log('Dataset is undefined or not an array');
                            return;
                        }

                        // 切换数据集的显示状态
                        dataset.hidden = !dataset.hidden;
                        legend.chart.update();
                    }
                },
                zoom: {
                    pan: {
                        enabled: true,
                        mode: 'x',
                    },
                    zoom: {
                        mode: 'x',
                        wheel: {
                            enabled: true
                        },
                        pinch: {
                            enabled: true
                        }
                    }
                }
            };
            option.responsive = true;
            option.maintainAspectRatio = false;
            console.log(option);
            this.chart = new Chart(
                canvasElement,
                {
                    type: 'line',
                    data: {
                        datasets: dataset,
                    },
                    options: option
                }
            );
        }
    }
}
</script>

<style>
#myapp {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    /* Full height of the viewport */
}

.chart-container {
    width: 80%;
    height: 80%;
    /* max-width: 800px;
  max-height: 600px; */
}

#myChart {
    width: 100% !important;
    height: 100% !important;
}
</style>